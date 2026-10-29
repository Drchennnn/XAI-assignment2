"""Run the agreed ImageNet-1K V1 models on a labeled image manifest."""
import argparse
import csv
import json
from pathlib import Path
import platform
import sys
import time

import torch
import torchvision
from PIL import Image
from torchvision.models import (
    resnet50, ResNet50_Weights,
    mobilenet_v3_large, MobileNet_V3_Large_Weights,
)

def predict(image_dir, manifest_path, output_path, cache_dir, batch_size=8):
    torch.set_num_threads(min(8, torch.get_num_threads()))
    torch.hub.set_dir(str(Path(cache_dir).resolve()))
    records = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    rw = ResNet50_Weights.IMAGENET1K_V1
    mw = MobileNet_V3_Large_Weights.IMAGENET1K_V1
    categories = rw.meta['categories']
    assert categories == mw.meta['categories']
    rt, mt = rw.transforms(), mw.transforms()
    assert repr(rt) == repr(mt), 'Official V1 transforms differ in this environment'
    print('Loading ResNet50 IMAGENET1K_V1', flush=True)
    resnet = resnet50(weights=rw, progress=False).eval()
    print('Loading MobileNetV3 Large IMAGENET1K_V1', flush=True)
    mobile = mobilenet_v3_large(weights=mw, progress=False).eval()
    results = []
    start = time.time()
    for offset in range(0, len(records), batch_size):
        chunk = records[offset:offset + batch_size]
        tensors_r, tensors_m = [], []
        for row in chunk:
            with Image.open(Path(image_dir) / row['original_filename']) as im:
                rgb = im.convert('RGB')
                xr, xm = rt(rgb), mt(rgb)
                assert torch.equal(xr, xm), 'Different model input tensors'
                tensors_r.append(xr)
                tensors_m.append(xm)
        with torch.inference_mode():
            rp = resnet(torch.stack(tensors_r)).softmax(dim=1)
            mp = mobile(torch.stack(tensors_m)).softmax(dim=1)
        for row, pr, pm in zip(chunk, rp, mp):
            gt = int(row['ground_truth_id'])
            ri, mi = int(pr.argmax()), int(pm.argmax())
            rc, mc = ri == gt, mi == gt
            group = 'A' if rc and mc else 'B' if rc else 'C' if mc else 'D'
            out = dict(row)
            out.update(ground_truth_class=categories[gt], group=group,
                       common_target_id=gt, common_target_class=categories[gt])
            for prefix, probs, idx, correct in [('resnet50', pr, ri, rc), ('mobilenetv3', pm, mi, mc)]:
                vals, ids = probs.topk(5)
                top5 = [dict(class_id=int(i), class_name=categories[int(i)], confidence=float(v)) for v, i in zip(vals, ids)]
                out.update({f'{prefix}_pred_id': idx, f'{prefix}_pred_class': categories[idx],
                            f'{prefix}_confidence': float(probs[idx]), f'{prefix}_correct': correct,
                            f'{prefix}_ground_truth_score': float(probs[gt]),
                            f'{prefix}_target_id': idx, f'{prefix}_top5_json': json.dumps(top5)})
            results.append(out)
        print(f'predicted {min(offset + batch_size, len(records))}/{len(records)}', flush=True)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0]))
        w.writeheader()
        w.writerows(results)
    metadata = dict(python=sys.version, platform=platform.platform(), torch=torch.__version__,
                    torchvision=torchvision.__version__, device='cpu', num_threads=torch.get_num_threads(),
                    resnet50_weights=str(rw), mobilenetv3_weights=str(mw), transforms=repr(rt),
                    class_index_base=0, confidence='softmax probability of the top-1 predicted class',
                    timing_seconds=round(time.time() - start, 3), candidate_count=len(results),
                    group_counts={g: sum(x['group'] == g for x in results) for g in 'ABCD'})
    output_path.with_suffix('.metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    print(json.dumps(metadata, ensure_ascii=False, indent=2), flush=True)
    return results

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--image-dir', type=Path, default=here / 'images')
    p.add_argument('--manifest', type=Path, default=here / 'manifest.json')
    p.add_argument('--out', type=Path, default=here / 'predictions_rerun.csv')
    p.add_argument('--cache-dir', type=Path, default=here / 'model_cache')
    p.add_argument('--batch-size', type=int, default=8)
    args = p.parse_args()
    predict(args.image_dir, args.manifest, args.out, args.cache_dir, args.batch_size)

# Member 1: Shared Dataset and Prediction Baseline

## Delivered

- `manifest.json`: 20 selected image records, labels, image IDs, source references, and SHA256 hashes.
- `configuration.json`: model versions, preprocessing, environment, selection rule, and limitations.
- `predictions.csv`: ResNet50 and MobileNetV3-Large predictions and confidence values for the selected 20 examples.
- `references/all_128_candidate_predictions.csv`: prediction record for the 128-image candidate pool.
- `predict.py`: code to rerun both model predictions when the authorized images are present.
- `member1_experiment.ipynb`: sanitized experiment notebook with outputs cleared.

## Locked setup

- ResNet50 `ResNet50_Weights.IMAGENET1K_V1`.
- MobileNetV3-Large `MobileNet_V3_Large_Weights.IMAGENET1K_V1`.
- Each model uses its official `weights.transforms()`; the recorded V1 preprocessing is resize 256, center crop 224, and ImageNet mean/std normalization.
- A/B/C/D each contain five selected examples: both correct, ResNet50 only correct, MobileNetV3 only correct, both incorrect.
- Selection used validation indices 1-128 and the first five distinct ground-truth classes per group in original index order. It was not ranked by confidence or explanation appearance.

## Reproduce

The public package omits the ImageNet images. Obtain the authorized 20 originals separately and place them under `member1/images/` using the names in `manifest.json`. From the repository root, install the dependencies listed by the handoff and run `python member1/predict.py --image-dir member1/images --manifest member1/manifest.json --out member1/predictions_rerun.csv --cache-dir member1/model_cache`.

The prediction script in this package uses the manifest's original filenames and writes a rerun CSV plus metadata. Model weights are not included. The experiment used Python 3.12.5, PyTorch 2.14.1+cpu, Torchvision 0.29.1+cpu, CPU, and 8 threads.

## Limitations

These 20 cases were intentionally balanced by joint correctness, from a small, non-random pool. Their group counts must not be used as overall accuracy estimates. Prediction confidence is a softmax score, not a calibrated probability claim.

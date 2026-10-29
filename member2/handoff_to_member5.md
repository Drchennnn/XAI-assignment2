# Handoff: Member 2 ResNet50 Results

## Files and completion status

- Notebook: `member2/Assignment2_成员2_ResNet50_XAI.ipynb`
- Result table: `member2/results/resnet50_xai_results.csv`
- Summary and settings: `member2/README.md`

Member 2's assigned experimental runs are complete: 20 primary model-prediction targets plus 15 supplementary shared-ground-truth targets for B/C/D, for 35 rows total. Locally, all 35 figures were generated and opened successfully. Image-derived PNGs are excluded from this public repository; after authorized images are placed locally, the notebook can regenerate them under `outputs/resnet50/`.

## Validation

- All expected sample/target combinations are present with no duplicates.
- All 20 ResNet50 top-1 labels match Member 1's predictions; maximum confidence difference is approximately 1.58e-6.
- Groups A/B/C/D each have five examples. This balanced case selection is not a population-accuracy evaluation.
- In group B, ResNet50's `pred` and `common_gt` targets are identical. Reuse the primary visualization where appropriate; do not count the pair as independent evidence.

## Cases for group synthesis

| Sample | Recorded result | Cautious observation |
|---|---|---|
| A01 | True/predicted sea snake; confidence 0.561. | Grad-CAM and LIME include the snake region; IG is more spatially fragmented. |
| B01 | ResNet50 predicts Shetland sheepdog correctly; MobileNetV3 predicts collie. | Useful same-image comparison; ResNet50 IG absolute delta is 0.822, so interpret its IG map cautiously. |
| C01 | True table lamp; ResNet50 predicts guillotine at 0.998 confidence. | `pred` and `common_gt` maps differ because their target classes differ. The crop excludes much of the lampshade, but crop causality was not tested. |
| D03 | True garter snake; ResNet50 predicts sea snake at 0.395 confidence. | Attribution near the snake does not mean the fine-grained class was identified correctly. |

These observations describe the selected figures; they do not prove why a model erred.

## Numerical caveat

For primary `pred` runs, absolute IG convergence delta has median approximately 0.292, ranges from approximately 0.122 to 0.974, and exceeds 0.5 for 7 of 20 cases. Diagnostics at 64/128/256 steps were recorded for B02 (0.974/0.084/0.095), C05 (0.750/0.418/0.120), and D01 (0.544/0.158/0.041). These checks measured delta only; higher-step attribution figures were not saved as replacement results.

## Integration steps

1. Pair Member 3's results by image ID, method, target mode, and target class. For cross-model spatial comparison, confirm the same source image and report each model's prediction alongside the shared target.
2. Add Member 4's method only after confirming it was not introduced in the course material; include its rationale and limitations.
3. Use multiple examples to answer whether the models' explanations look similar. Distinguish visual overlap from causal evidence, and mention the balanced sample design and IG delta caveat.
4. Member 2 still contributes one meme and one personal video segment; the complete video should be assembled with all members' own segments and remain within two minutes.

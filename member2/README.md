# Member 2: ResNet50 XAI

## Responsibility

Run the three confirmed classroom methods, Grad-CAM, Integrated Gradients (IG), and LIME, on ResNet50 using the shared examples from Member 1. Keep each model input tied to the original image and ResNet50 V1's official transforms. Use the model's own top-1 class for the main `pred` analysis and the shared ground-truth class for B/C/D supplementary `common_gt` comparisons.

## Delivered and verified

- `Assignment2_成员2_ResNet50_XAI.ipynb`: experiment code, parameter descriptions, sample-level interpretations, cross-sample observations, and limitations.
- `results/resnet50_xai_results.csv`: 35 records: 20 `pred` runs plus 15 B/C/D `common_gt` runs.
- `handoff_to_member5.md`: integration notes, representative cases, and caveats.
- All 35 explanation figures were generated and inspected locally; the figure files are omitted from this public package with the ImageNet-derived image assets.

The 20 ResNet50 top-1 labels matched Member 1's baseline; the largest confidence difference was approximately 1.58e-6. There are five examples in each group. In group B, ResNet50 is correct, so its `pred` and `common_gt` targets are the same and should not be described as independent evidence.

## Method settings

- Weights: `ResNet50_Weights.IMAGENET1K_V1`; weight-provided resize/crop/normalization transforms.
- Grad-CAM target layer: `layer4[-1]`.
- IG: normalized all-zero baseline (the ImageNet mean-color input), 64 steps; convergence delta is reported as a numerical approximation diagnostic.
- LIME: 224x224 transformed crop, quickshift default segmentation, 500 perturbations, at most 10 displayed superpixels, black occlusion, batch size 32, seed 2026.
- Experiment environment recorded in the local run: Python 3.12.14, PyTorch 2.14.1, Torchvision 0.29.1, Captum 0.9.0, LIME 0.2.0.1, scikit-image 0.26.0, Apple MPS.

## Key findings and limitations

The notebook discusses A01, B01, C01, and D03 as concrete cases. C01 is a wrong table-lamp example where the target changes from the predicted `guillotine` class to the true `table lamp` class; the attribution pattern changes with the target. The central crop excludes much of the original lampshade, which is a hypothesis for further testing, not a demonstrated cause of the error. D03 shows that highlighting a snake region does not guarantee correct fine-grained classification.

Across the 20 primary `pred` runs, median absolute IG convergence delta is about 0.292; 7/20 exceed 0.5. Higher deltas warrant caution about the 64-step approximation. Step-count diagnostics were run for B02, C05, and D01 only; they did not replace the saved formal results. LIME depends on superpixel and perturbation settings. Method visualizations do not establish causal reasoning.

The final cross-model question remains open until Member 3 supplies aligned MobileNetV3 results and Member 4 supplies the new-method results.

# Selected Research Question

## Assignment prompt

The team chose **question 2** from `Assignment2-2026A.ipynb`: whether different CNNs use similar feature-extraction approaches and classification evidence.

## Our narrowed question

> For the same ImageNet examples, do ResNet50 and MobileNetV3-Large explanations highlight similar image regions? How do their explanations differ when one or both models predict incorrectly?

The models are pretrained ImageNet-1K CNNs using the explicit Torchvision V1 weights:

- ResNet50: `ResNet50_Weights.IMAGENET1K_V1`
- MobileNetV3-Large: `MobileNet_V3_Large_Weights.IMAGENET1K_V1`

Both use their weights' official preprocessing transforms (RGB, resize shorter side to 256, center crop to 224, ImageNet normalization). The explanation set is shared by image ID; the two models are not retrained or adjusted to equalize accuracy.

## Sample groups

Member 1 selected 20 examples, five per group:

| Group | ResNet50 | MobileNetV3-Large |
|---|---|---|
| A | Correct | Correct |
| B | Correct | Incorrect |
| C | Incorrect | Correct |
| D | Incorrect | Incorrect |

The candidate pool was ImageNet validation indices 1-128. Within each group, examples were selected in original index order, choosing the first five distinct ground-truth classes. Because groups were deliberately balanced and the candidate pool is small and non-random, these examples do not estimate either model's overall accuracy.

## Explanation targets and methods

Members 2 and 3 use the same three classroom methods on their assigned models: Grad-CAM, Integrated Gradients, and LIME. The primary `pred` target is each model's own top-1 class. For B/C/D, the supplementary `common_gt` target is the same ground-truth class for both models. The target mode must be stated in each comparison: a `common_gt` explanation does not mean the model predicted that class.

Member 4 will add one new method, to be checked against course lectures/tutorials, and run it on both models. Member 5 will synthesize the evidence across models and methods after those results exist.

## Evidence boundary

At present, the repository includes Member 1's prediction baseline and Member 2's ResNet50 XAI results only. It cannot yet answer whether the two models attend to similar regions overall. Heatmaps are method-dependent evidence about attribution under a chosen target; they do not prove causal mechanisms or why a model made an error.

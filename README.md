# CS5495 Assignment 2: XAI for CNNs

This repository contains the team's Assignment 2 materials. The current package covers Member 1's shared ImageNet sample and prediction baseline, and Member 2's ResNet50 explanations using Grad-CAM, Integrated Gradients (IG), and LIME.

## Research question

For the same ImageNet examples, do ResNet50 and MobileNetV3-Large explanations highlight similar image regions? How do their explanations differ on examples where one or both models are wrong?

This is the team's chosen version of question 2 in the assignment notebook. It is a case-study comparison, not a claim about overall model accuracy or causal reasoning.

## Contents

- `docs/assignment_requirements.md`: assignment deliverables, deadlines, rubric, and video/Q&A requirements.
- `docs/research_question.md`: selected question, scope, and comparison protocol.
- `docs/team_division.md`: five-member ownership and deliverables.
- `member1/`: sample manifest, labels, model predictions, configuration, prediction code, and sanitized notebook.
- `member2/`: ResNet50 XAI notebook, result table, and handoff for Member 5.
- `member3/`, `member4/`, `member5/`: reserved for the remaining contributions.

## Status

- Member 1: shared 20-image sample and both-model baseline prepared; A/B/C/D each contain five examples.
- Member 2: 35 ResNet50 XAI runs completed and documented (20 model-prediction targets plus 15 shared-ground-truth targets for B/C/D).
- Members 3-5: reserved; their results and final group-level conclusions are not included yet.

## Data and reproducibility

ImageNet source images, model weights, image crops, contact sheets, and image-derived explanation figures are not included in this public repository. The metadata and result tables are included. To rerun the notebooks, obtain the authorized sample images separately, put the 20 selected originals under `member1/images/` using the filenames in `member1/manifest.json`, and launch Jupyter from the repository root. The Member 2 notebook expects the manifest, predictions, and images to be available locally.

Model weights are downloaded through Torchvision on first run. Member 1's environment versions and Member 2's experiment settings are documented in their respective READMEs and notebooks. Results are from a small, intentionally balanced case set and must not be presented as population accuracy.

## Assignment submissions

The course submission still requires all investigation notebooks, a PDF containing the notebooks, two meme images, presentation slides, a video of no more than two minutes, and a TBL contribution statement. The video and final merged coursework deliverables are not yet in this repository. See `docs/assignment_requirements.md`.

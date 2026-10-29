# Team Division and Handoff

| Member | Ownership | Required contribution | Status |
|---|---|---|---|
| 1 | Shared data and two-model baseline | Curate shared ImageNet examples; document selection, labels, weights, preprocessing, and predictions from both models. | Prepared; public package contains metadata and prediction tables, while images remain local. |
| 2 | ResNet50 classroom XAI | Run Grad-CAM, IG, and LIME; document parameters, results, interpretations, and limitations; prepare one meme and a short personal video segment. | XAI runs and handoff are complete; meme/video segment still need final team integration. |
| 3 | MobileNetV3-Large classroom XAI | Run the same three methods on the same images, aligned target policy, and document comparable outputs. | Reserved; awaiting contribution. |
| 4 | New XAI method | Confirm one method not covered in class; justify it and run it on both models with documented settings/results. | Reserved; method and contribution pending. |
| 5 | Synthesis and final quality check | Compare model/method results, answer the research question with evidence, integrate notebook/report, coordinate slides/video/PDF, and check final submission. | Reserved; depends on Members 3 and 4 results. |

Each member should explain their own experimental evidence in the notebook. For the video, each person records their own short segment; the group combines the segments into one video under two minutes. The video should focus on the question and findings, not enumerate the task assignments. The course asks the group to show the memes before discussing the XAI analysis and to state the group number.

## Handoff path

- Member 1: `member1/README.md`
- Member 2: `member2/README.md` and `member2/handoff_to_member5.md`
- Members 3-5: add their own README, notebook/results, and an explicit handoff status under their reserved directories.

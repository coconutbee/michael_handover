# Latest Research on Face Recognition
### Dataset Descriptions

- **RepSet-X-S**  
  透過將 27K ID 低於 10 張的圖像刪除所得到  

- **RepSet-X-S-P**  
  ID 都加入 3 張 DMD 的 Pose 擴增，CFP-FP 指標所以有效  

- **RepSet-X-S-A**  
  ID 都加入 3 張 DMD 的 Age 擴增，雖然 CALFW 有提升但 AgeDB 下降不少，所以無效  

- **RepSet-X-S-V**  
  ID 都加入 10 張 Vec2face 的擴增 (全正臉無變化)，大多都有提升，所以有效  

- **RepSet-X-S-V-C**  
  在 RepSet-X-S-V 上挑選TFace分數最高的圖片進行複製5張圖片擴增

- **RepSet-X-S-V-P**  
  在 RepSet-X-S-V 上每個 ID 再加入 3 張 DMD 的 Pose 擴增，CFP-FP 指標所以有效  

- **RepSet-X-S-V-P-A**  
  在 RepSet-X-S-V-P 上每個 ID 再加入 3 張 DMD 的 Age 擴增，效能退步無效  

- **RepSet-X-S-V-P-D**  
  在 RepSet-X-S-V-P 上每個 ID 再加入 5 張 DCFace 擴增，全體效能提升故有效  

### Training from scratch

| Datasets | Subjects/Images | Method/Arch | LFW | CFP-FP | AgeDB | CPLFW | CALFW | Avg. | Effective? |
|----------|-----------------|-------------|-----|--------|-------|-------|-------|------|------------|
| **Baseline Datasets** |  |  |  |  |  |  |  |  |  |
| MS1MV2 | 85K / 5.8M |  | 99.80 | 98.40 | 98.20 | 92.90 | 96.03 | 97.07 |  |
| DCFace | 10K / 0.55M |  | 99.07 | 91.13 | 92.25 | 86.28 | 93.10 | 92.36 |  |
| CemiFace | 10K / 0.55M |  | 99.18 | 90.96 | 93.12 | 87.57 | 93.55 | 92.88 |  |
| Vec2Face | 10K / 0.50M |  | 97.93 | 84.29 | 89.90 | 81.00 | 91.95 | 89.01 |  |
| UIFace | 10K / 0.50M |  | 99.23 | 92.20 | 92.50 | 88.08 | 93.17 | 93.04 |  |
| **Our Experiments** |  |  |  |  |  |  |  |  |  |
| RepSet-X-38K | 38K / 0.35M | ArcFace/IR50 | 99.23 | 92.19 | 92.68 | 88.50 | 93.72 | 93.26 |  |
| RepSet-X-S | 10K / 0.21 M | ArcFace/IR50 | 97.68 | 85.50 | 86.83 | 81.20 | 89.68 | 88.18 |  |
| +P | 10K / 0.24 M | ArcFace/IR50 | 97.50 | 86.16 | 86.38 | 80.82 | 89.42 | 88.06 | V |
| +A | 10K / 0.24 M | ArcFace/IR50 | 97.48 | 86.31 | 86.00 | 80.90 | 90.03 | 88.14 | X |
| +V | 10K / 0.31 M | ArcFace/IR50 | 97.98 | 86.02 | 88.20 | 81.82 | 91.23 | 89.05 | V |
| +V、C | 10K / 0.36 M | ArcFace/IR50 | 98.22 | 86.67  | 88.07 | 81.47 | 91.08 | 89.10 | - |
| +V、P | 10K / 0.34 M | ArcFace/IR50 | 98.17 | 87.03 | 87.58 | 82.37 | 90.98 | 89.23 | V |
| +V、P、A | 10K / 0.37 M | ArcFace/IR50 | 98.15 | 86.00 | 87.30 | 82.13 | 90.58 | 88.83 | X |
| +V、P、D | 10K / 0.39 M | ArcFace/IR50 | 98.33 | 87.06 | 88.38 | 83.20 | 91.34 | 89.66 | V |
| +V、P、D、C | 10K / 0.44 M | ArcFace/IR50 | 98.33 | 87.06 | 88.38 | 83.20 | 91.34 | 89.66 | V |
### Distilled from glint_cosface_r50

| Datasets         | Subjects/Images | Method/Arch   | LFW   | CFP-FP | AgeDB | CPLFW | CALFW | Avg.  |
|------------------|-----------------|---------------|-------|--------|-------|-------|-------|-------|
| RepSet-X-S-V-P-D | 10K / 0.39 M    | ArcFace/IR50 | 99.06 | 91.42  | 92.55 | 93.18 | 88.03 | 92.85 |


### Dataset Paths
ROOT = `/media/avlab/8TB/Michael/arcface_torch_LR_50/gradeuate/dataset/images/reduce_size`
| Datasets | Subjects/Images | Path |
|----------|-----------------|------|
| RepSet-X-S | 10K / 0.21 M | `ROOT/RepSet_X_15` |
| +P | 10K / 0.24 M | `ROOT/RepSet_X_15_pose` |
| +A | 10K / 0.24 M | `ROOT/RepSet_X_15_age` |
| +V | 10K / 0.31 M | `ROOT/RepSet_X_15_vec2face` |
| +V、C | 10K / 0.36 M | `ROOT/RepSet_X_15_vec2face_c` |
| +V、P | 10K / 0.34 M | `ROOT/RepSet_X_15_vec2face_pose` |
| +V、P、A | 10K / 0.37 M | `ROOT/RepSet_X_15_vec2face_pose_age` |
| +V、P、D | 10K / 0.39 M | `ROOT/RepSet_X_15_vec2face_pose_dcface` |

## Previous Research
統整過往研究release的Training dataset, code與合成資料
- DCFace [CVPR 2023]: [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Kim_DCFace_Synthetic_Face_Generation_With_Dual_Condition_Diffusion_Model_CVPR_2023_paper.pdf)
- CemiFace [NeurIPS 2024]: [paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/3ec6c6fc9065aa57785eb05dffe7c3db-Paper-Conference.pdf)
- Vec2Face [ICLR 2025]: [paper](https://arxiv.org/pdf/2409.02979)
- UIFace [ICLR 2025]: [paper](https://arxiv.org/pdf/2502.19803)

#### UIFace also release a testing code for evaluating the quality of synthetic data [link](https://github.com/Tencent/TFace/blob/master/recognition/test/README.md).

| Method | training data | training code | synthetic data | Reproducible |
|--------|---------------|---------------|----------------|--------------|
| [DCFcace](https://github.com/mk-minchul/dcface?tab=readme-ov-file) | [&#10004;][Various dataset](https://github.com/deepinsight/insightface/tree/master/recognition/_datasets_) | [&#10004;][link](https://github.com/mk-minchul/dcface?tab=readme-ov-file) | [&#10004;][link](https://drive.google.com/drive/folders/1bbG2P3pz81ujj-Ss1mOLol3qnQhc4nBJ) | [&#10004;] |
| [CemiFace](https://github.com/szlbiubiubiu/CemiFace) | [&#10004;][CASIAWebFace](https://drive.google.com/file/d/1KxNCrXzln0lal3N4JiYl9cFOIhT78y1l/view)、[VggFace2](https://www.kaggle.com/datasets/hearfool/vggface2) | [&#10006;] | [&#10004;][link](https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL3UvYy83YmQ1ODQ5MWM1NGU0MzUxL0VlN3Y5X09Qck5kTmlwb183U2hvMVhvQjc0T2dPUGVlSi1PUnpYTVM4YVcyYmc%5FZT12ajdyTDA&cid=7BD58491C54E4351&id=7BD58491C54E4351%21sf3f7efeeac8f4dd78a9a3fed2868d57a&parId=7BD58491C54E4351%21s5d42798c6ca94d20b6fd213146f7793e&o=OneUp) | [&#10006;] |
| [Vec2Face](https://github.com/HaiyuWu/Vec2Face) | [&#10004;][WebFace4M](https://huggingface.co/datasets/gaunernst/webface4m-wds-gz) | [&#10004;][link](https://github.com/HaiyuWu/Vec2Face?tab=readme-ov-file) | [&#10004;][link](https://github.com/HaiyuWu/Vec2Face?tab=readme-ov-file) | [&#10004;] |
| [UIFace](https://github.com/Tencent/TFace/tree/master/generation/uiface) | [&#10004;][CASIAWebFace](https://drive.google.com/file/d/1KxNCrXzln0lal3N4JiYl9cFOIhT78y1l/view) | [&#10004;][link](https://github.com/Tencent/TFace/tree/master/generation/uiface) | [&#10004;][link](https://drive.google.com/drive/folders/1rYk9b0jv1eX4H2X1F8JmX4Zt5c3KX1mN) | [&#10004;] |

## Note:
- RepSet_X_15的ID: `ROOT/RepSet_X_15_id`
- 除了DMD之外，也可以用vec2face擴充，就是用上面的ID然後用vec2face的生成器生成: `ROOT/Vec2Face`
## Vec2face - [github](https://github.com/HaiyuWu/Vec2Face)
```bash
python image_generation_with_reference.py --image_file "path/of/the/image/file or folder" --model_weights weights/vec2face_generator.pth --batch_size 5 --example 10 --name images-of-references
```
- Best dataset: `ROOT/RepSet_X_15_vec2face_pose` #Augmentation with DMD & vec2face

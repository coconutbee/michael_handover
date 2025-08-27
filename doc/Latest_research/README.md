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
| Vec2Face | 10K / 0.50M |  | 99.10 | 88.71 | 91.43 | 85.93 | 92.72 | 91.58 |  |
| UIFace | 10K / 0.50M |  | 99.23 | 92.20 | 92.50 | 88.08 | 93.17 | 93.04 |  |
| **Our Experiments** |  |  |  |  |  |  |  |  |  |
| RepSet-X-S | 10K / 0.21 M | ArcFace/IR50 | 97.68 | 85.50 | 86.83 | 81.20 | 89.68 | 88.18 |  |
| +P | 10K / 0.24 M | ArcFace/IR50 | 97.50 | 86.16 | 86.38 | 80.82 | 89.42 | 88.06 | V |
| +A | 10K / 0.24 M | ArcFace/IR50 | 97.48 | 86.31 | 86.00 | 80.90 | 90.03 | 88.14 | X |
| +V | 10K / 0.31 M | ArcFace/IR50 | 97.98 | 86.02 | 88.20 | 81.82 | 91.23 | 89.05 | V |
| +V、C | 10K / 0.36 M | ArcFace/IR50 | 97.98 | 86.02 | 88.20 | 81.82 | 91.23 | 89.05 | V |
| +V、P | 10K / 0.34 M | ArcFace/IR50 | 98.17 | 87.03 | 87.58 | 82.37 | 90.98 | 89.23 | V |
| +V、P、A | 10K / 0.37 M | ArcFace/IR50 | 98.15 | 86.00 | 87.30 | 82.13 | 90.58 | 88.83 | X |
| +V、P、D | 10K / 0.39 M | ArcFace/IR50 | 98.33 | 87.06 | 88.38 | 83.20 | 91.34 | 89.66 | V |

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



## Note:
- RepSet_X_15的ID: `ROOT/RepSet_X_15_id`
- 除了DMD之外，也可以用vec2face擴充，就是用上面的ID然後用vec2face的生成器生成: `ROOT/Vec2Face`
## Vec2face - [github](https://github.com/HaiyuWu/Vec2Face)
```bash
python image_generation_with_reference.py --image_file "path/of/the/image/file or folder" --model_weights weights/vec2face_generator.pth --batch_size 5 --example 10 --name images-of-references
```
- Best dataset: `ROOT/RepSet_X_15_vec2face_pose` #Augmentation with DMD & vec2face

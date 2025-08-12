# Part 3: DMD(Dual Modal Diffusion)
## Step 1: Data location
- CAF-Aug: /media/avlab/disco/Michael/CAF_dataset/Cross_Age_Face_crop_age_aug_label # on 1601191353
- Vox2-LP: /media/avlab/disco/Michael/vox2/vox2_label # on 1601191353
## Note:
### Age label:
- MiVOLO Path: /media/michaeljison/2TB/Michael/MiVOLO # on 1414974416
- Usage: python label_age.py --input <dataset_path> --detector-weights <yolo_ckpt_path> --checkpoint <mivolo_ckpt_path>
##### Example:
```bash
python label_age.py --input /media/michaeljison/2TB/caf_age_ana/output/caf_50-69 --detector-weights /media/michaeljison/2TB/Michael/MiVOLO/models/yolov8x_person_face.pt --checkpoint /media/michaeljison/2TB/Michael/MiVOLO/models/mivolo_imbd.pth.tar
```
### Angle label:
- Path: /media/michaeljison/2TB/Michael/cal_reggie_metrics # on 1414974416
- Usage: python label_angle.py
#### Label logic: <folder_name>_<num_img>_<yaw>_<age_mivolo>.jpg
![labbel_logic](label_logic.png)
## Step 2: Train the DMD model
```bash
bash train.sh 
```
Datamodule path :/media/avlab/8TB/Michael/dcface/dcface/src/configs/datamodule/caf.yaml
![yaml_set](yaml_set.png)

## Step 3: Inference
- Path: /media/avlab/8TB/Michael/dcface/dcface/src
```bash
bash synthesis.sh
```
![Inference](dcface_inference.png)
ID_IMAGES_ROOT: ID images path (without subfolders, only ID)
STYLE_IMAGES_ROOT: style images path(with subfolder, also ID corresponding with images) 
OUTPUT_ROOT: output path

## Supplementary
### all pose and age transformation ckpt locations
![ckpt_locations](ckpt_locations.png)
![ckpt_locations](ckpt_locations-2.png)
### DEMO code
- Path: /media/avlab/8TB/Michael/dcface/dcface # on 1601191353
```bash
python app.py
```
![Demo](dcface_demo.png)
#### Details:
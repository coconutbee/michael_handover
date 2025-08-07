# Part 1: Prepare base model for ArcFace
## Step 1: Data compression
```bash
python -m mxnet.tools.im2rec --list --recursive train <dataset_path> # list the images in the dataset

python -m mxnet.tools.im2rec train.lst <dataset_path> # create the record file
```
- path of dataset: /media/avlab/8TB/Michael/arcface_torch_LR_50/gradeuate/dataset/images/RepSet_X_7 #on 1601191353
* [ x ] Dataset compression completed, and .rec, .list, and .idx files have been obtained.

## Step 2: Set the config file
- config.py: RepSet_X_7.py
![arcface_config](arcface_config.png)
## Step 3: Train the base model
```bash
python train_v2.py configs/config/<config.py>
```
Validation while training. Also shows the validation accuracy, you can only force on 'Accuracy-Highest' value.

- config.py: RepSet_X_7.py
## Step 4: Validation
![arcface_val](arcface_val.png)
```bash
python verification_torch.py
```
# Part 2: AdaDistillation
## Step 1: Data compression
```bash
python -m mxnet.tools.im2rec --list --recursive train <dataset_path> # list the images in the dataset

python -m mxnet.tools.im2rec train.lst <dataset_path> # create the record file
```
- path of dataset: /media/avlab/8TB/Michael/arcface_torch_LR_50/gradeuate/dataset/images/RepSet_X_7 #on 1601191353
* [ x ] Dataset compression completed, and .rec, .list, and .idx files have been obtained.
## Step 2: Set the config file
- config.py: RepSet_X_7.py
![KD_config-1](KD_config-1.png)
![KD_config-2](KD_config-2.png)
## Step 3: Train the AdaDistillation model
```bash
bash run_AdaDistill.sh # Backbone used for test value. Header used for train resume.
```
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
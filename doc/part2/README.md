# Part 2: AdaDistillation

## Step 1: Data compression
```bash
python -m mxnet.tools.im2rec --list --recursive train <dataset_path>  # list the images in the dataset
python -m mxnet.tools.im2rec train.lst <dataset_path>                 # create the record file
```
- Path of dataset: /media/avlab/8TB/Michael/arcface_torch_LR_50/gradeuate/dataset/images/RepSet_X_7 #on 1601191353
- [ x ] Dataset compression completed, and .rec, .list, and .idx files have been obtained.

## Step 2: Set the config file
- `config.py`: `RepSet_X_7.py`

![KD_config-1](KD_config-1.png)
![KD_config-2](KD_config-2.png)

## Step 3: Train the AdaDistillation model
```bash
bash run_AdaDistill.sh  # Backbone used for test value. Header used for train resume.
```

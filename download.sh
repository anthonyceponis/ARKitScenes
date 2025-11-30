#!/bin/sh

DATA_DIR=data
mkdir -p $DATA_DIR
python3 download_data.py upsampling --split Training --video_id_csv depth_upsampling/upsampling_train_val_splits.csv --download_dir $DATA_DIR

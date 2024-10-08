# -*- coding: utf-8 -*-
"""drone_yolov7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YUuo0XkZnxIIds9fAq3aD-T3kyLvJ_e4
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/WongKinYiu/yolov7.git
# %cd yolov7
!pip install -r requirements.txt

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="3bXBPVkbSV6ZrhAQMGV3")
project = rf.workspace("drone-piulw").project("drone_detection-tf5ig")
version = project.version(3)
dataset = version.download("yolov7")

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov7
!python train.py --batch-size 16 --cfg cfg/training/yolov7.yaml --epochs 1 --data /content/yolov7/Drone_detection-3/data.yaml --weights yolov7.pt --device 0

!python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source {dataset.location}/test/images

import glob
from IPython.display import Image, display

i = 0
limit = 100 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): # assuming JPG
    if i < limit:
        display(Image(filename=imageName))
        print("\n")
    i += 1

import glob
from IPython.display import Image, display

i = 0
limit = 10 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): # assuming JPG
    if i < limit:
        display(Image(filename=imageName))
        print("\n")
    i += 1
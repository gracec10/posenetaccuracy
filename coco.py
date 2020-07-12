from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import random
import os
import cv2
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

### For visualizing the outputs ###
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

annFile='../COCOdataset2017/val.json'

# Initialize the COCO api for instance annotations
coco=COCO(annFile)

annIDs = coco.getAnnIds(catIds=1, iscrowd=False)
anns = coco.loadAnns(annIDs)

imgs_gt = []
imgs = []

for x in anns:
    imgID = x.get('image_id')
    kp = x.get('keypoints')

    if any (i != 0 for i in kp[0:20]) == True and imgID not in [d['imgID'] for d in imgs_gt]:
        url = coco.loadImgs(imgID)[0].get('coco_url')
        img_dict = {
            "imgID": imgID,
            "nose_x": kp[0],
            "nose_y": kp[1],
            "l_eye_x": kp[3],
            "l_eye_y": kp[4],
            "r_eye_x": kp[6],
            "r_eye_y": kp[7],
            "l_ear_x": kp[9],
            "l_ear_y": kp[10],
            "r_ear_x": kp[12],
            "r_ear_y": kp[13],
            "l_shoulder_x": kp[15],
            "l_shoulder_y": kp[16],
            "r_shoulder_x": kp[18],
            "r_shoulder_y": kp[19],
            "url": url
        }
        imgs_gt.append(img_dict)
        imgs.append(imgID)

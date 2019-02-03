import cv2
import os
from advertisement.models import load_yolo

def detect(file_path):
    tfnet = load_yolo()
    detected = 0
    count = 0
    for image in os.listdir(file_path):
        try:
            image_path = file_path + '/' + image
            print(image_path)
            imgcv = cv2.imread(image_path)
            print(imgcv.shape,"shape")
            result = tfnet.return_predict(imgcv)
            print(len(result))
            count += 1
            if len(result)>1:
                detected = detected + 1
        except:
            continue
    return detected, count
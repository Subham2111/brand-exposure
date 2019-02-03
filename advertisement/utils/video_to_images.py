import cv2
import numpy as np
import cv2
import uuid


def convert(file,jpg_path):
    try:
        vidcap = cv2.VideoCapture(file)
        success, image = vidcap.read()
        count = 0
        success = True
        while success:
            success, image = vidcap.read()
            save_path = jpg_path + '/' + str(uuid.uuid4())[:4] + '.jpg'
            cv2.imwrite(save_path, image)  # save frame as JPEG file
            if cv2.waitKey(10) == 27:  # exit if Escape is hit
                break
            count += 1
    except:
        pass
    return jpg_path

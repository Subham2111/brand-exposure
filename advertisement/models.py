from django.db import models
from advertisement import admin
import os
from advertisement.resources.darkflow.darkflow.net.build import TFNet

def load_yolo():
    os.chdir(admin.darkflow_path)
    options = {
        'model': admin.model_path,
        'load': 1000,
        'threshold': 0.12
    }

    tfnet = TFNet(options)
    return tfnet

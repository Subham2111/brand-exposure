from django.contrib import admin
from untitled4 import settings
# Register your models here.
base_dir = settings.BASE_DIR
origin_path = base_dir + '/media'
base_path = base_dir+ '/advertisement/resources'
temp_path = base_path + '/temp_path'
jpg_path = temp_path + '/jpg_path'
text_path = temp_path + '/text_path'
darkflow_path = base_path + '/darkflow'
model_path = base_path + '/darkflow/cfg/tiny-yolo-1c.cfg'
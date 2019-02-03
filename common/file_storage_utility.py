import os
import uuid

from django.core.files.storage import default_storage
import shutil
import uuid


def saveFileWithTimestamp(file, origin_path):
    if file:
        ext = file.name.split('.')[-1]
        file_name = str(uuid.uuid4())[:4] + '.' + ext
        path = default_storage.save(file_name, file)
        print(path)
        save_path = origin_path + '/' + file_name
        return save_path


def deleteFolder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)


def createFolder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name, 0o775)
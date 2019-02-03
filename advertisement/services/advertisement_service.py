from advertisement import admin
from common import file_storage_utility
from common import check_extension
from advertisement.utils import video_to_images, detect_image,decision


class AdvertisementServiceClass:
    def __init__(self,file,valid):
        self.file = file.strip()
        self.valid = valid.strip()
        self.base_path = admin.base_path
        self.temp_path = admin.temp_path
        self.TEXT_PATH = admin.text_path
        self.jpg_path = admin.jpg_path
        file_storage_utility.deleteFolder(self.temp_path)
        file_storage_utility.createFolder(self.temp_path)
        file_storage_utility.createFolder(self.TEXT_PATH)
        file_storage_utility.createFolder(self.jpg_path)
        pass


    def advertisement_service(self):
        result, message, status_code, status=check_extension.check_extension(self.file)
        if status_code==400:
            final_dict = {'result': result, 'message': message, 'status_code': status_code, 'status': status}
            return final_dict,status_code
        result = video_to_images.convert(self.file, self.jpg_path)
        detected, total = detect_image.detect(self.jpg_path)
        result, message = decision.decision(detected, total, self.valid)
        final_dict = {'result': result, 'message': message}
        return final_dict, 200


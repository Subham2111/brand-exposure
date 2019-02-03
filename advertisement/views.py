from django.shortcuts import render
from rest_framework.response import Response
from common import file_storage_utility
from advertisement import admin
from rest_framework.views import APIView
from advertisement.services.advertisement_service import AdvertisementServiceClass

class AdvertisementClass(APIView):
    def post(self, request, *args, **kwargs):
        file_storage_utility.deleteFolder(admin.origin_path)
        file_storage_utility.createFolder(admin.origin_path)
        json_data = request.data
        print(json_data)
        keys = list(request.POST)
        print(keys)
        try:
            file = json_data['video']
        except KeyError:
            file = None
        try:
           valid = json_data['valid_percentage']
        except KeyError:
            valid = None
        try:
            file = file.strip()
            valid = valid.strip()
        except AttributeError:
            file = file_storage_utility.saveFileWithTimestamp(file, admin.origin_path)
            if file is None or file == '':
                file = ''
            if valid is None or valid == '':
                valid = ''
        advert_obj =AdvertisementServiceClass(file, valid)
        final_dict, status_code = advert_obj.advertisement_service()
        return Response(final_dict, status=status_code)

    pass



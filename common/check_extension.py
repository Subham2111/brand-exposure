"""
Problem:
  Check even if the extension is not .jpeg, .jpg, .tiff, .pdf, .png
"""

import os


def check_extension(filename):
    print(filename)
    extension_list = ['.avi', '.mkv', '.webm']
    try:
        stem, ext = os.path.splitext(filename)
        print(ext)
        if not ext:
            status_code = 400
            message = 'No extension present in the image'
            result = None
            status = 'error'
            return result, message, status_code, status 
        else:
            if ext.lower() not in extension_list:
                status_code = 400
                message = '{} format of document is not supported'.format(ext.lower())
                result = None
                status = 'error'
                return result, message, status_code, status 
            else:
                status_code = 200
                message = None
                result = (stem, ext.lower())
                status = 'Success'
                return result, message, status_code, status 
    except:
        status_code = 400
        message = 'Error in Checking file Extension'
        result = None
        status = 'error'
        return result, message, status_code, status 



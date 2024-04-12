import os.path
import sys
import yaml
import base64
import platform

from isd.exception import isdException
from isd.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise isdException(e, sys) from e


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
def detect_os():
    system = platform.system()
    if system == 'Windows':
        return "Windows"
    elif system == 'Linux':
        return "Linux"
    elif system == 'Darwin':
        return "Mac"
    else:
        return "Unknown"

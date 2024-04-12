from isd.exception import isdException
from isd.configuration.s3_operations import S3Operation
from isd.entity.config_entity import ModelPusherConfig
import sys,os


def download_model_s3()-> str:
    '''
    Fetch data from s3
    '''
    try:
        model_pusher_config = ModelPusherConfig()
        s3 = S3Operation()
    except Exception as e:
        raise isdException(e, sys)

    try: 
        
        model_download_dir = "yolov7"+"/"+model_pusher_config.S3_MODEL_KEY_PATH
        
        if os.path.exists(model_download_dir):
            print(f"File already exists: {model_download_dir}")
        else:
            # Download the file from S3 bucket
            s3.download_object(
                key= model_pusher_config.S3_MODEL_KEY_PATH, 
                bucket_name= model_pusher_config.MODEL_BUCKET_NAME,
                filename = model_download_dir
            )
            print(f"File downloaded successfully from S3 bucket: {model_pusher_config.MODEL_BUCKET_NAME}/{model_pusher_config.S3_MODEL_KEY_PATH}")
        return model_download_dir

    except Exception as e:
        raise isdException(e, sys)
    

download_model_s3()
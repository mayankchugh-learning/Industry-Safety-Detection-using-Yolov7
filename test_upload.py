from isd.exception import isdException
from isd.configuration.s3_operations import S3Operation
from isd.entity.config_entity import ModelPusherConfig
import sys,os


def upload_model_s3():
    '''
    Fetch data from s3
    '''
    try:
        model_pusher_config = ModelPusherConfig()
        s3 = S3Operation()
    except Exception as e:
        raise isdException(e, sys)

    trained_model_file_path = '/Users/mayankchugh/gitRepos/mayankchugh.learning/Industry-Safety-Detection-using-Yolov7/yolov7/best.pt'
    try: 
        # Uploading the best model to s3 bucket
            s3.upload_file(
                trained_model_file_path,
                model_pusher_config.S3_MODEL_KEY_PATH,
                model_pusher_config.MODEL_BUCKET_NAME,
                remove=False,
            )
            print("Uploaded best.pt model to s3 bucket")
    except Exception as e:
        raise isdException(e, sys)
    

upload_model_s3()
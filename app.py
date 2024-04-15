import sys,os
from isd.pipeline.training_pipeline import TrainPipeline
from isd.exception import isdException
from isd.utils.main_utils import decodeImage, encodeImageIntoBase64, detect_os
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from isd.configuration.s3_operations import S3Operation
from isd.entity.config_entity import ModelPusherConfig
from isd.logger import logging


app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return 
    


@app.route("/")
def home():
    return render_template("index.html")

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
            logging.info(f"File already exists: {model_download_dir}")
        else:
            # Download the file from S3 bucket
            s3.download_object(
                key= model_pusher_config.S3_MODEL_KEY_PATH, 
                bucket_name= model_pusher_config.MODEL_BUCKET_NAME,
                filename = model_download_dir
            )
            logging.info(f"File downloaded successfully from S3 bucket: {model_pusher_config.MODEL_BUCKET_NAME}/{model_pusher_config.S3_MODEL_KEY_PATH}")
        return model_pusher_config.S3_MODEL_KEY_PATH

    except Exception as e:
        raise isdException(e, sys)


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        os.system("rm -rf yolov7/runs")
        image = request.json['image']
        decodeImage(image, clApp.filename)

        model_file = download_model_s3()
        logging.info("sucess downloaded model_file: ")

        os_string = detect_os()
        print("Operating System OS_string ß: ",os_string)

        if os_string == "Linux":
            os.system("cd yolov7/ && python3 detect.py --weights best.pt  --source ../data/inputImage.jpg")
        else:
            os.system("cd yolov7/ && python detect.py --weights best.pt  --source ../data/inputImage.jpg")

        logging.info("next command downloaded model_file: ")

        if os.path.exists("yolov7/runs/detect/exp/inputImage.jpg"):
            logging.info(f"File path yolov7/runs/detect/exp/inputImage.jpg already exists")
        else:
           os.system("cd yolov7/ && mkdir runs")
           os.system("cd yolov7/runs && mkdir detect")
           os.system("cd yolov7/runs/detect && mkdir exp")


        opencodedbase64 = encodeImageIntoBase64("yolov7/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov7/runs")

    except ValueError as val:
        logging.info(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        logging.info(e)
        result = "Invalid input"

    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8000)
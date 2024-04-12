import sys,os
from isd.exception import isdException
from isd.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from isd.configuration.s3_operations import S3Operation
from isd.entity.config_entity import ModelPusherConfig
from isd.logger import logging





app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "flaskdrive"

def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = S3Operation()
    response = s3_client.upload_file(file_name, object_name, bucket)

    return response

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = S3Operation()
    output = f"downloads/{file_name}"
    s3.download_object(file_name, output)

    return output


@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route("/storage")
def storage():
    contents = list_files("m-isd-data-2024")
    return render_template('storage.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload_file(f"uploads/{f.filename}", BUCKET)

        return redirect("/storage")

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
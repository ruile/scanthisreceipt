import os
import cv2

from flask import Flask, request
from werkzeug.utils import secure_filename

from ocr import ocr_model

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
UPLOAD_FOLDER = './upload'
if not os.path.isdir(UPLOAD_FOLDER):
	os.makedirs(UPLOAD_FOLDER) 

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def health():
	return "Hello!"

@app.route('/scan', methods=["POST"])
def scan():
	if "file" not in request.files:
		return { "error": "no file" }, 400

	file = request.files['file']
	if file.filename == '':
		return { "error": "invalid file" }, 400
	if file and allowed_file(file.filename):
		print("file", file)
		filename = secure_filename(file.filename)
		filepath = os.path.join(UPLOAD_FOLDER, filename)
		file.save(filepath)
		print("filename", filename)
		img = cv2.imread(filepath)
		result = ocr_model.scan(img)

		# delete file
		os.remove(filepath)

	return { "data": result }, 200
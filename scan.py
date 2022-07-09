from flask import (
	Blueprint, request
)

bp = Blueprint("scan", __name__, url_prefix="/scan")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @bp.route("/", methods=["POST"])
# def scan():
# 	if "file" not in request.files:
# 		return { "error": "no file" }, 400

# 	file = request.files['file']
# 	if file.filename == '':
# 		return { "error": "invalid file" }, 400
# 	if file and allowed_file(file.filename):
# 		filename = secure_filename(file.filename)
# 		img = cv2.imread(filename)

# 		ocr.ocr
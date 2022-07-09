from flask import Flask
from singleton import ocr
import cv2

app = Flask(__name__)

@app.route('/')
def health():
	return "Hello!"

@app.route('/test')
def test():
	img = cv2.imread('test_images/close.png')

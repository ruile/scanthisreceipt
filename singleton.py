import os
from cv2 import detail_DpSeamFinder
from paddleocr import PaddleOCR, draw_ocr

det_dir = "./models/en_PP-OCRv3_det_infer"
rec_dir = "./models/en_PP-OCRv3_rec_infer"

ocr = PaddleOCR(lang="en", det_model_dir=det_dir, rec_model_dir=rec_dir)

def test(path):
	result = ocr.ocr(path, cls=True)
	for line in result:
		print(line)

base = "test_images"
test(os.path.join(base, "close2.jpg"))
import re
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

DET_DIR = "./models/en_PP-OCRv3_det_infer"
REC_DIR = "./models/en_PP-OCRv3_rec_infer"

DICTIONARY = {
	"PERISHABLE_DRINK": ["MK", "MILK", "JUICE"],
	"FISH": ["BASS", "SALMON", "SABA", "TUNA", "SWORDFISH"],
	"FRUIT": ["BANANA", "APPLE", "ORANGE", "PEACH", "DURIAN", "KIWI", "PEAR", "GRAPE"],
	"VEGETABLE": ["ONION", "TOMATO", "PANDAN", "CAI", "LETTUCE", "CUCUMBER"],
	"MEAT": ["CHICKEN", "BEEF", "LAMB", "PORK"]
}

MULTIPLE = re.compile(r"\d+X\$")

class OCR():
	def __init__(self):
		self.model = PaddleOCR(lang="en", det_model_dir=DET_DIR, rec_model_dir=REC_DIR, use_angle_cls=False)

	def scan(self, img):
		result = self.model.ocr(img, cls=False)
		items = []
		
		for i in range(len(result) - 1):
			line1 = result[i][1][0]
			line2 = result[i + 1][1][0]

			detected_category = None

			if line1[0].isalpha() and "Price" not in line1:
				has_cateogory = False
				for category, words in DICTIONARY.items():
					for word in words:
						if word in line1:
							detected_category = category
							itemObj = {"name": line1, "category": detected_category}
							items.append(itemObj)
							has_cateogory = True
				
				if not has_cateogory:
					detected_category = "UNCATEGORISED"
					itemObj = {"name": line1, "category": detected_category}
					items.append(itemObj)
			else:
				continue

			mo = MULTIPLE.search(line2)
			# print('mo', mo)
			if mo and mo.group():
				itemObj = {"name": line1, "category": detected_category}
				quantity = int(line2.split("X")[0])

				for i in range(quantity - 1):
					items.append(itemObj)

		return items

ocr_model = OCR()
import pytesseract
import cv2
from pdf2image import convert_from_path
import os
import uuid
import re

def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)

    return text

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image):
    """
    Improve OCR accuracy
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)[1]
    return thresh


def extract_text(file_path: str) -> str:
    text = ""

    try:
        # 📄 Case 1: PDF
        if file_path.lower().endswith(".pdf"):
            images = convert_from_path(file_path)

            for img in images:
                temp_filename = f"temp_{uuid.uuid4().hex}.jpg"
                img.save(temp_filename, "JPEG")

                image = cv2.imread(temp_filename)
                processed = preprocess_image(image)

                text += pytesseract.image_to_string(processed)

                os.remove(temp_filename)

        # 🖼️ Case 2: Image
        else:
            image = cv2.imread(file_path)

            if image is None:
                return ""

            processed = preprocess_image(image)
            text = pytesseract.image_to_string(processed)

    except Exception as e:
        print("OCR Error:", str(e))
        return ""

    return text
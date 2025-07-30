
import pytesseract
from PIL import Image

def extract_text_from_image(image_path, lang="eng"):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()

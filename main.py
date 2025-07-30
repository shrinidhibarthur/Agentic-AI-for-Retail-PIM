
from modules.copywriter import generate_product_copy
from modules.tagger import tag_attributes
from modules.image_to_video import create_video_from_image
from modules.image_to_text import extract_text_from_image
import json

def main():
    with open("config/config.json") as f:
        config = json.load(f)

    product_image = "data/sample_product.jpg"

    print("📝 Generating product copy...")
    description = generate_product_copy("Red cotton t-shirt")
    print(description)

    print("🏷️ Tagging attributes...")
    tags = tag_attributes(description)
    print(tags)

    print("🖼️ Extracting text from image...")
    text_in_image = extract_text_from_image(product_image, config["ocr_lang"])
    print(text_in_image)

    print("🎥 Creating product video...")
    create_video_from_image(product_image, "data/product_video.mp4")
    print("✅ Done! Video saved at data/product_video.mp4")

if __name__ == "__main__":
    main()

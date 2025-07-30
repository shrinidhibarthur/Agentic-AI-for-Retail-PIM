
import asyncio
import json
import os
import sys
import pandas as pd
from multiprocessing import Pool, cpu_count
from modules.copywriter import generate_product_copy
from modules.tagger import tag_attributes
from modules.image_to_video import create_video_from_image
from modules.image_to_text import extract_text_from_image

def load_config():
    with open("config/config.json") as f:
        return json.load(f)

async def process_sku(sku, config):
    description = generate_product_copy(sku["name"], config["openai_api_key"])
    tags = tag_attributes(description)
    ocr_text = extract_text_from_image(sku["image_path"], config["ocr_lang"])
    video_path = f"data/videos/{sku['id']}.mp4"
    create_video_from_image(sku["image_path"], video_path)
    return {
        "sku_id": sku["id"],
        "description": description,
        "tags": tags,
        "ocr_text": ocr_text,
        "video_path": video_path
    }

async def process_batch(batch, config):
    tasks = [process_sku(sku, config) for sku in batch]
    return await asyncio.gather(*tasks)

def batch_worker(args):
    batch, config = args
    return asyncio.run(process_batch(batch, config))

def run_pipeline(all_skus, config):
    batch_size = config.get("batch_size", 1000)
    max_workers = config.get("max_workers", cpu_count())
    batches = [all_skus[i:i+batch_size] for i in range(0, len(all_skus), batch_size)]
    with Pool(max_workers) as p:
        results = p.map(batch_worker, [(batch, config) for batch in batches])
    return [sku for batch_result in results for sku in batch_result]

if __name__ == "__main__":
    config = load_config()
    os.makedirs("data/videos", exist_ok=True)

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        print("🚀 Running in DEMO mode using sample_skus.csv")
        all_skus = pd.read_csv("data/sample_skus.csv").to_dict(orient="records")
    else:
        all_skus = [{"id": i, "name": f"Product {i}", "image_path": "data/sample_product.jpg"} for i in range(150000)]
    
    print(f"📦 Processing {len(all_skus)} SKUs...")
    processed_data = run_pipeline(all_skus, config)
    print(f"✅ Completed processing {len(processed_data)} SKUs.")

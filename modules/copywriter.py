
import openai
import os

def generate_product_copy(product_name):
    openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    prompt = f"Write a professional, engaging product description for: {product_name}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

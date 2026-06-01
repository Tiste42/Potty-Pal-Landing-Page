import os
import io
from PIL import Image
from google import genai
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY") or "AIzaSyBFFBuhG66P5epXLoGHuaDQEIk9pwBGuH8"

PROMPT = (
    "A cheerful toddler with rosy cheeks sitting in a warm bubble bath in a "
    "cozy family bathroom, happily playing with a yellow rubber duck and a "
    "small toy boat. Soft fluffy white bubbles, gentle steam rising. A patient, "
    "smiling parent kneels beside the tub holding a fluffy hooded towel. A small "
    "pastel teal potty chair sits on the bath mat nearby. Warm golden bathroom "
    "light, soft pastel tile, friendly natural details. Illustration style: classic "
    "American children's picture book, similar to Richard Scarry or Berenstain Bears. "
    "Simple, friendly, warm. No text, no words, no logos, no letters, no numbers."
)

OUT_PATH = os.path.join("images", "blog", "toddler-pees-in-bath.webp")


def main():
    client = genai.Client(api_key=API_KEY)
    print("Generating hero image with Imagen 4.0 Ultra ...")
    response = client.models.generate_images(
        model="imagen-4.0-ultra-generate-001",
        prompt=PROMPT,
        config=types.GenerateImagesConfig(number_of_images=1),
    )

    img_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    print("Source size:", img.size)

    target_w, target_h = 1200, 675

    scale = target_w / img.width
    new_w = target_w
    new_h = int(img.height * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    if new_h < target_h:
        scale = target_h / img.height
        new_w = int(img.width * scale)
        new_h = target_h
        img = img.resize((new_w, new_h), Image.LANCZOS)

    left = (img.width - target_w) // 2
    top = (img.height - target_h) // 2
    img = img.crop((left, top, left + target_w, top + target_h))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    img.save(OUT_PATH, "WEBP", quality=85)
    print(f"Saved {OUT_PATH} ({img.size})")


if __name__ == "__main__":
    main()

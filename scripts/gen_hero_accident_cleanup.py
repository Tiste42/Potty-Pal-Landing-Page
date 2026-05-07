import os
import io
from google import genai
from google.genai import types
from PIL import Image

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyBFFBuhG66P5epXLoGHuaDQEIk9pwBGuH8")
SLUG = "potty-training-accident-cleanup"

PROMPT = (
    "A cheerful family living room scene where a calm, smiling parent is gently "
    "cleaning a small spot on a cozy couch cushion with a cloth and a spray bottle, "
    "while a curious toddler in a t-shirt and underwear stands nearby holding a small "
    "wipe to help, and a happy little potty chair sits on a colorful rug in the "
    "background. Warm sunlight, friendly pastel colors, soft and welcoming. "
    "Illustration style: classic American children's picture book, similar to "
    "Richard Scarry or Berenstain Bears. Simple, friendly, warm. "
    "No text, no words, no logos, no letters, no numbers."
)


def main():
    client = genai.Client(api_key=API_KEY)
    print("Generating image with Imagen 4.0 Ultra...")
    response = client.models.generate_images(
        model="imagen-4.0-ultra-generate-001",
        prompt=PROMPT,
        config=types.GenerateImagesConfig(number_of_images=1),
    )

    img_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    print(f"Source image size: {img.size}")

    target_w, target_h = 1200, 675

    # Fit width first
    scale = target_w / img.width
    new_w = target_w
    new_h = int(round(img.height * scale))
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # If too short, scale by height instead
    if new_h < target_h:
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        scale = target_h / img.height
        new_w = int(round(img.width * scale))
        new_h = target_h
        img = img.resize((new_w, new_h), Image.LANCZOS)

    # Center crop to exactly 1200x675
    left = (img.width - target_w) // 2
    top = (img.height - target_h) // 2
    img = img.crop((left, top, left + target_w, top + target_h))

    out_path = os.path.join("images", "blog", f"{SLUG}.webp")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "WEBP", quality=85)
    print(f"Saved: {out_path}  ({img.size})")


if __name__ == "__main__":
    main()

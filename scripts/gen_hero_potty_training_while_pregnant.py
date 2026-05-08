import os
import io
from google import genai
from google.genai import types
from PIL import Image

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyBFFBuhG66P5epXLoGHuaDQEIk9pwBGuH8")
SLUG = "potty-training-while-pregnant"
OUT_PATH = os.path.join("images", "blog", f"{SLUG}.webp")

PROMPT = (
    "A warm sunny scene inside a cozy home: a pregnant parent with a visible "
    "round belly sitting comfortably on a low floor cushion, smiling at a happy "
    "toddler who is sitting on a small colorful potty chair nearby. The parent "
    "is gently giving a thumbs up. Soft natural light through a window, a potted "
    "plant, a small basket of clean clothes nearby, a rug on the floor. "
    "Illustration style: classic American children's picture book, similar to "
    "Richard Scarry or Berenstain Bears. Simple, friendly, warm, rounded shapes, "
    "soft outlines, gentle pastel colors. No text, no words, no logos, no letters, "
    "no numbers."
)

def main():
    client = genai.Client(api_key=API_KEY)
    print("Generating with Imagen 4.0 Ultra...")
    response = client.models.generate_images(
        model="imagen-4.0-ultra-generate-001",
        prompt=PROMPT,
        config=types.GenerateImagesConfig(number_of_images=1),
    )
    img_bytes = response.generated_images[0].image.image_bytes
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    print(f"Source: {img.size}")

    scale = 1200 / img.width
    new_h = int(img.height * scale)
    img_r = img.resize((1200, new_h), Image.LANCZOS)
    if img_r.height < 675:
        scale2 = 675 / img.height
        new_w = int(img.width * scale2)
        img_r = img.resize((new_w, 675), Image.LANCZOS)
        left = (new_w - 1200) // 2
        img_final = img_r.crop((left, 0, left + 1200, 675))
    else:
        top = (img_r.height - 675) // 2
        img_final = img_r.crop((0, top, 1200, top + 675))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    img_final.save(OUT_PATH, "WEBP", quality=85)
    print(f"Saved: {OUT_PATH} -> {img_final.size}")

if __name__ == "__main__":
    main()

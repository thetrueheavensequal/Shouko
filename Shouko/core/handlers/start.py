from core.dispatcher import app
from pyrogram import filters
import random
from pathlib import Path

def get_komi_image():
    images_path = Path("F:/Dev/Shouko/Shouko/static/komi_images")
    images = list(images_path.glob("*.jpg")) + list(images_path.glob("*.png"))
    return str(random.choice(images)) if images else None

@app.on_message(filters.command("start"))
async def komi_start(client, message):
    img = get_komi_image()
    text = (
        "こ、こんにちは... I'm Komi Shouko! I hope we can be friends...\n"
        "(Use /help to see what I can do!)"
    )
    if img:
        await message.reply_photo(img, caption=text)
    else:
        await message.reply(text)
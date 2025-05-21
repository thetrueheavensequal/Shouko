from pyrogram import filters
from core.dispatcher import app
import random
from pathlib import Path

def get_komi_image():
    images = list(Path("F:/Dev/Shouko/Shouko/static/komi_images").glob("*.jpg")) + \
             list(Path("F:/Dev/Shouko/Shouko/static/komi_images").glob("*.png"))
    return str(random.choice(images)) if images else None

@app.on_message(filters.command("start"))
async def komi_start(client, message):
    img = get_komi_image()
    await message.reply_photo(
        img,
        caption="こ、こんにちは... I'm Komi Shouko! I hope we can be friends... (Please use /help if you need anything...)"
    ) if img else await message.reply(
        "こ、こんにちは... I'm Komi Shouko! I hope we can be friends... (Please use /help if you need anything...)"
    )

@app.on_message(filters.command("help"))
async def komi_help(client, message):
    img = get_komi_image()
    help_text = (
        "📝 **Komi's Notebook of Commands**\n"
        "/start - Komi shyly greets you\n"
        "/help - Komi's notebook (this message)\n"
        "/afk - Komi will let others know you're away\n"
        "/ban - Komi (politely) removes someone\n"
        "/anime - Komi helps you find anime info\n"
        "/waifu - Komi shares a cute waifu (maybe herself?)\n"
        "/pat - Komi sends a pat gif\n"
        "/ping - Komi checks her heartbeat\n"
        "…and more, all in Komi style!"
    )
    await message.reply_photo(img, caption=help_text) if img else await message.reply(help_text)
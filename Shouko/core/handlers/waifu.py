import requests  # Add this at the top

from pyrogram import filters
from core.dispatcher import app

@app.on_message(filters.command("waifu"))
async def waifu_image(client, message):
    resp = requests.get("https://api.waifu.pics/sfw/waifu").json()
    await message.reply_photo(resp["url"])
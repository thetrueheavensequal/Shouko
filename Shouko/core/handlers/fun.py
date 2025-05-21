import requests
from core.dispatcher import app
from pyrogram import filters

@app.on_message(filters.command("pat"))
async def komi_pat(client, message):
    resp = requests.get("https://api.waifu.pics/sfw/pat").json()
    await message.reply_animation(resp["url"], caption="(writes on notebook) Komi gives you a gentle pat...")
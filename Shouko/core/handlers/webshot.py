from pyrogram import Client, filters
import requests
from io import BytesIO
from core.dispatcher import app
from PIL import Image



@app.on_message(filters.command("shot") & filters.private)
async def screenshot_handler(client, message):
    args = message.text.split()
    if len (args) < 2:
        await message.reply("Please provide a URL...")
        return
    url = args[1]
    full = 'true' if len(args) > 2 and args[2].lower() == 'full' else 'false'
    api_url = f"https://api.safone.co/webshot?url={url}&full={full}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        image = BytesIO(response.content)
        image.name = "webshot.png"
        
        await message.reply_photo(photo=image, caption=f"Screenshot of the website has been taken, Here you go...")
        
    except Exception as e:
        await message.reply(f"Failed to fetch screenshot.\nError: {e}")

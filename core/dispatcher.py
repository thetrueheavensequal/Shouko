from pyrogram import Client, filters
from django.conf import settings
from core.tasks import process_message

app = Client(
    "Shouko",
    api_id=settings.TG_API_ID,
    api_hash=settings.TG_API_HASH,
    bot_token=settings.TG_BOT_TOKEN,
)

@app.on_message(filters.text & filters.private)
async def handle_message(client, message):
    result = process_message.delay(message.text)
    await message.reply(f"Processing your message: {message.text}")
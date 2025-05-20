from pyrogram import Client, filters
from django.conf import settings
from core.tasks import process_message

app = Client(
    "Shouko",
    api_id=settings.TG_API_ID,
    api_hash=settings.TG_API_HASH,
    bot_token=settings.TG_BOT_TOKEN,
)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    await message.reply(
        "こ、こんにちは... I'm Shouko Komi. If you have something you'd like to talk about, please send me a message. I'll do my best to reply...! (Even if it's a little difficult for me sometimes.)"
    )

@app.on_message(filters.command("help") & filters.private)
async def help_handler(client, message):
    await message.reply(
        "You can send me any message, and I'll try to respond as best as I can. If I seem quiet, please be patient with me... Let's become friends!"
    )

@app.on_message(filters.text & filters.private & ~filters.command(["start", "help"]))
async def ai_response(client, message):
    if message.from_user and message.from_user.is_self:
        return
    process_message.delay(message.text, message.chat.id)
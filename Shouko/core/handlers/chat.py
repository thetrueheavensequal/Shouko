from core.dispatcher import app
from pyrogram import filters

@app.on_message(filters.text & ~filters.command(["start", "help", "ping", "waifu", "pat"]) & ~filters.me)
async def komi_chat(client, message):
    # You can call your AI/celery task here, or reply with a Komi-fied message
    # Example: call your process_message task
    from core.tasks import process_message
    process_message.delay(message.text, message.chat.id)
    await message.reply("(writes on notebook) ...Komi is thinking...")
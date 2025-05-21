from pyrogram import filters
from core.dispatcher import app

@app.on_message(filters.command("anime"))
async def komi_anime(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("Komi tilts her head... Please use: /anime <title>")
        return
    # ... (API call as before)
    await message.reply(f"📖 Komi found this anime for you: ...")
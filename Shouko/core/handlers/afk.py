afk_users = {}  # Add this at the top

from pyrogram import filters
from core.dispatcher import app

@app.on_message(filters.command("afk"))
async def komi_afk(client, message):
    reason = " ".join(message.command[1:]) or "Komi is quietly away…"
    afk_users[message.from_user.id] = reason
    await message.reply(f"✏️ Komi wrote in her notebook: You're AFK! Reason: {reason}")
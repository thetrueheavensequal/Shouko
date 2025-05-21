from core.dispatcher import app
from pyrogram import filters

@app.on_message(filters.new_chat_members)
async def komi_welcome(client, message):
    for member in message.new_chat_members:
        await message.reply(f"Komi shyly waves at {member.mention}… Welcome to the group!")
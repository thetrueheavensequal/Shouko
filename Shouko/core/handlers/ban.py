from pyrogram import filters
from core.dispatcher import app

@app.on_message(filters.command("ban") & filters.group)
async def komi_ban(client, message):
    if not message.reply_to_message:
        await message.reply("Komi looks confused... Please reply to a user's message to ban them.")
        return
    user_id = message.reply_to_message.from_user.id
    await client.kick_chat_member(message.chat.id, user_id)
    await message.reply("Komi shyly points to the exit... User has been removed.")
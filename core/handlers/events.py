from pyrogram import Client, filters
from core.dispatcher import app

@app.on_message(filters.new_chat_members)
async def welcome_new_member(client, message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            await message.reply(f"Hello! I'm {member.first_name}, Thanks for adding me to the group!")
        else:
            await message.reply(f"Welcome {member.first_name}! Glad to have you here.")
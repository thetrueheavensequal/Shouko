from pyrogram import Client, filters
from django.conf import settings
from core.dispatcher import app 

admin_users = [settings.ADMIN_USER_ID]

@app.on_message(filters.command("start") & filters.user(admin_users))
async def start(client, message):
    await message.reply("Welcome to the admin panel! Use /help to see available commands.")
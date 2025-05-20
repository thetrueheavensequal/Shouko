from pyrogram import Client, filters
from core.dispatcher import app

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome to the bot! Use /help to see available commands.")
@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply(
        "Available commands:\n/start - Start the bot\n/help - Show this help message")
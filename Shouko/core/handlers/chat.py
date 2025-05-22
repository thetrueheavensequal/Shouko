from core.dispatcher import app
from pyrogram import filters
from pyrogram.types import Message


# Group chat replies only — when someone replies *to Komi*
@app.on_message(
    filters.group & filters.text & 
    ~filters.command(["start", "help", "ping", "waifu", "pat"]) & 
    ~filters.me
)
async def komi_group_reply(client, message: Message):
    # Ignore if it's not a reply
    if not message.reply_to_message:
        return

    # Get Komi bot's own user ID
    bot_user = await client.get_me()

    # Ignore if not replying to Komi
    if message.reply_to_message.from_user.id != bot_user.id:
        return

    from core.tasks import process_message
    process_message.delay(message.text, message.chat.id)
    await message.reply("(writes on notebook) ...Komi is thinking...")


# Private chat conversations — respond unless it's a command
@app.on_message(
    filters.private & filters.text & 
    ~filters.command(["start", "help", "ping", "waifu", "pat"]) & 
    ~filters.me
)
async def komi_private_chat(client, message: Message):
    from core.tasks import process_message
    process_message.delay(message.text, message.chat.id)
    await message.reply("(blushes) ...O-oh... um... okay... desu.")

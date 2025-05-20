from pyrogram import Client, filters
from core.dispatcher import app
from core.tasks import process_message

@app.on_message(filters.text & filters.private)
async def ai_response(client, message):
    #Delegate to celery task for gemini api processing
    result = process_message.delay(message.text)
    await message.reply(f"Processing your message: {message.text}")
    # You can also send the result back to the user once it's ready
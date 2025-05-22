import time  # Add this at the top

from pyrogram import filters
from core.dispatcher import app

@app.on_message(filters.command("ping"))
async def komi_ping(client, message):
    start = time.time()
    m = await message.reply("Komi is checking her heartbeat…")
    end = time.time()
    await m.edit(f"❤️~ Komi's heartbeat: `{int((end-start)*1000)}ms` ~❤️")
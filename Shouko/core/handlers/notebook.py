from pyrogram import Client, filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton, Message
)
import random
from config import API_ID, API_HASH, BOT_TOKEN

# Quiet and cute note-style images
KOMI_NOTE_IMAGES = [
    "https://files.catbox.moe/enzetg.jpg",
    "https://files.catbox.moe/lc46od.jpg",
    "https://files.catbox.moe/ee82s3.jpg",
    "https://files.catbox.moe/jygtws.jpg"
]

app = Client("KomiBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

notes_db = {}

async def get_bot_username():
    me = await app.get_me()
    return me.username

@app.on_message(filters.command("start") & filters.private)
async def start_message(_, message: Message):
    bot_username = await get_bot_username()
    intro = (
        "Um... h-hi...\n"
        "I'm Komi...\n"
        "(blushes)\n\n"
        "You can send a quiet note to someone...\n"
        "Just tap the button below to start...\n\n"
        "I... hope it helps..."
    )
    image = random.choice(KOMI_NOTE_IMAGES)
    
    await message.reply_photo(
        photo=image,
        caption=intro,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✍️ Send a note", switch_inline_query="")]]
        )
    )

async def _whisper(_, inline_query):
    data = inline_query.query.strip()
    results = []
    bot_username = await get_bot_username()
    
    if len(data.split()) < 2:
        return [
            InlineQueryResultArticle(
                title="✍️ Send a note",
                description=f"@{bot_username} [USERNAME or ID] [message]",
                input_message_content=InputTextMessageContent(
                    f"Um... try this:\n@{bot_username} @username Your message here..."
                ),
                thumb_url=random.choice(KOMI_NOTE_IMAGES),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✍️ Start", switch_inline_query="")]]
                )
            )
        ]
    
    try:
        target = data.split()[0]
        note = data.split(None, 1)[1]
        user = await app.get_users(target)
    except:
        return [
            InlineQueryResultArticle(
                title="✍️ Error...",
                description="Couldn't find that user...",
                input_message_content=InputTextMessageContent("Um... that username looks wrong..."),
                thumb_url=random.choice(KOMI_NOTE_IMAGES)
            )
        ]
    
    notes_db[f"{inline_query.from_user.id}_{user.id}"] = note

    markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("📩 Read note...", callback_data=f"note_{inline_query.from_user.id}_{user.id}")
    ]])
    
    return [
        InlineQueryResultArticle(
            title="📮 Note ready",
            description=f"Send a note to @{user.username}" if user.username else f"Send a note to {user.first_name}",
            input_message_content=InputTextMessageContent(
                f"(blushes)... I-I wrote something for you...\n\nClick to read it..."
            ),
            reply_markup=markup,
            thumb_url=random.choice(KOMI_NOTE_IMAGES)
        )
    ]

@app.on_callback_query(filters.regex(r"note_(.*)"))
async def reveal_note(_, query):
    _, from_id, to_id = query.data.split("_")
    from_id = int(from_id)
    to_id = int(to_id)
    viewer_id = query.from_user.id

    if viewer_id not in [from_id, to_id]:
        return await query.answer("U-um... this note isn't for you...", show_alert=True)

    try:
        note_text = notes_db[f"{from_id}_{to_id}"]
    except:
        note_text = "... I-I think the note is gone..."

    await query.answer(note_text, show_alert=True)

@app.on_inline_query()
async def bot_inline(_, inline_query):
    query_text = inline_query.query.strip().lower()

    if not query_text:
        return await inline_query.answer(await _whisper(_, inline_query), cache_time=0)
    else:
        return await inline_query.answer(await _whisper(_, inline_query), cache_time=0)
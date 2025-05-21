from core.dispatcher import app
from pyrogram import filters
import random
import json
import re
from pathlib import Path

NOTEBOOK_FILE = Path("F:/Dev/Shouko/Shouko/static/komi_notebook.json")

def load_notes():
    if NOTEBOOK_FILE.exists():
        with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTEBOOK_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

@app.on_message(filters.command(["note", "notebook"]) & filters.group & ~filters.me)
async def send_note(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply(
            "To send an anonymous note, use:\n"
            "/note user_id your message here\n\n"
            "For example: /note 123456789 Hello!"
        )
        return

    try:
        user_id = int(args[1])
        note = args[2].strip()
    except ValueError:
        await message.reply(
            "Please use a valid user ID number.\n"
            "Example: /note 123456789 Hello!"
        )
        return

    if not note:
        await message.reply("Please write a message after the user ID.")
        return

    # Rarely use the notebook phrase
    import random
    notebook_phrases = [
        "(writes on notebook)",
        "",
        "",
        "",
        "",
        "(scribbles quietly)",
        "",
        "",
        "",
        "",
    ]
    prefix = random.choice(notebook_phrases)

    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    # Hide note behind a button
    await message.reply(
        f"{prefix} Anonymous note for <code>{user_id}</code> is ready. Only the recipient can view it.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📬 View Note", callback_data=f"view_note_{user_id}")]
            ]
        )
    )

# Callback handler for the button
from pyrogram.types import CallbackQuery

@app.on_callback_query(filters.regex(r"^view_note_(\d+)$"))
async def reveal_note(client, callback_query: CallbackQuery):
    user_id = int(callback_query.matches[0].group(1))
    if callback_query.from_user.id != user_id:
        await callback_query.answer("This note isn't for you!", show_alert=True)
        return

    # Find the original note message (you may want to store notes in a dict or DB for production)
    # For demo, just parse from the replied message
    note_cmd = callback_query.message.reply_to_message
    if note_cmd and note_cmd.text:
        args = note_cmd.text.split(maxsplit=2)
        note = args[2] if len(args) > 2 else "No note found."
    else:
        note = "No note found."

    await callback_query.answer()
    await callback_query.message.reply(
        f"📖 Anonymous note for you:\n\n{note}",
        quote=True
    )
    await callback_query.message.delete()

@app.on_message(filters.command("readnote") & filters.private & ~filters.me)
async def read_note_instructions(client, message):
    await message.reply(
        "(writes on notebook) To send an anonymous note, use:\n"
        "/note user_id your message here\n\n"
        "For example: /note 123456789 Hello!\n"
        "(The user must have started me first)"
    )
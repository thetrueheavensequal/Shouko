from pyrogram import Client, filters
from django.conf import settings

# Global filter to ignore bot's own messages
ignore_bot_messages = ~filters.me

app = Client(
    "Shouko",
    api_id=settings.TG_API_ID,
    api_hash=settings.TG_API_HASH,
    bot_token=settings.TG_BOT_TOKEN,
)

""" alive, antinsfw, approve, blacklist,
blacklist_stickers, botadmins, bug, connection, cosplay, couple,
cust_filters, disable, disasters, extra, feds, flood, fsub, fun,
gban, hyperlink, imagegen, info, instadl, karma, locks, log_channel,
mute, nekomode, newuserinfo, notes, palmchat, pkang, pokedex,
purge, quotely, reverse, rules, sangmata, speedtest, sports,
stickers, telegraph, tr, unbanall, users, warns, whispers, zombies
 """

# Import all handlers to register their commands and events
from core.handlers import (
    admin, afk, anime, chat, ban, ping, search, notebook, fun, welcome, start, help, waifu  # add any new handler modules here
)
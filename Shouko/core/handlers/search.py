from core.dispatcher import app
from pyrogram import filters
from core.services.websearch import web_search
from core.tasks import process_message

@app.on_message(filters.command("search") & filters.private)
async def search_handler(client, message):
    query = " ".join(message.command[1:]).strip()
    if not query:
        await message.reply("(writes on notebook) Komi is waiting... Please tell me what you want to search for.")
        return

    results = web_search(query)
    if not results:
        await message.reply("(writes on notebook) ...Sorry, Komi couldn't find anything.")
        return

    summary_prompt = (
        f"Here are some web search results for '{query}':\n\n"
        + "\n\n".join([f"{r['title']}\n{r['href']}\n{r['body']}" for r in results])
        + "\n\nPlease summarize and present these as Shouko Komi would: shy, brief, polite, sometimes using (writes on notebook), and include any useful images as links."
    )
    # Send the summary prompt to the AI task queue
    process_message.delay(summary_prompt, message.chat.id)
    await message.reply("(writes on notebook) Komi is thinking... Please wait for the summary.")
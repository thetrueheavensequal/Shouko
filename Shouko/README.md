# Shouko 🤖

[![Build Status](https://github.com/thetrueheavensequal/Shouko/actions/workflows/ci.yml/badge.svg)](https://github.com/thetrueheavensequal/Shouko/actions)
[![License](https://img.shields.io/github/license/thetrueheavensequal/Shouko)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

A modular Telegram bot built with [Pyrogram](https://github.com/pyrogram/pyrogram) and [Django](https://www.djangoproject.com/), featuring Google Gemini-powered AI chat in the style of Shouko Komi, group management, and a web dashboard.

---

## ✨ Features

- **AI Chat:** Google Gemini integration, always in-character as Shouko Komi (from *Komi Can't Communicate*)
- **Personality:** Shouko's responses are brief, shy, and authentic, with self-knowledge as a Telegram bot created by [@hitorijainyo](https://t.me/hitorijainyo)
- **Group Admin Tools:** Ban, mute, promote, and more
- **Event Handling:** Welcome/goodbye messages, logging
- **Web Dashboard:** (Optional) Manage groups and view logs
- **Celery Tasks:** For background jobs and AI message processing
- **Procfile/Honcho:** Run bot and worker together in one terminal
- **Dockerized:** Easy deployment with Docker & Compose

---

## 🗂️ Project Structure

```
Shouko/
├── config/             # Django configuration and Celery app
├── core/               # Django app: models, views, tasks, dispatcher
├── static/             # Frontend assets
├── templates/          # HTML templates
├── manage.py
├── requirements.txt
├── Procfile
├── run_bot.py
├── .env
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/thetrueheavensequal/Shouko.git
cd Shouko/Shouko
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in your secrets (Telegram API ID, API hash, bot token, Gemini API key, etc).

### 3. Install dependencies

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the bot and Celery worker together

**Recommended:** Use [honcho](https://github.com/nickstenning/honcho) and the provided `Procfile`:

```bash
pip install honcho
honcho start
```

This will run both the Telegram bot and the Celery worker in one terminal.

---

## 🛠️ Configuration

- All Django settings are in `config/settings/`
- Use `.env` for secrets and environment-specific variables
- Gemini system prompt and Shouko's character are defined in `core/tasks.py`

---

## 🤖 AI Personality

- Shouko Komi always responds in-character: brief, shy, polite, sometimes using ellipses or written notes.
- She acknowledges being a Telegram bot and her creator (@hitorijainyo) if asked, but never breaks character.
- The system prompt is carefully crafted to enforce this style for every Gemini response.

---

## 🧩 Extending

- Add new bot commands or handlers in `core/dispatcher.py` or `core/handlers/`
- Add new models in `core/models.py`
- Add Celery tasks in `core/tasks.py`

---

## 🐳 Docker

To run with Docker:

```bash
docker-compose up --build
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests and issues are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## ⭐️ Show your support

Give a ⭐️ if you like this project!

---

**Made with ❤️ by [thetrueheavensequal](https://github.com/thetrueheavensequal)**

---

> _“Automate your Telegram groups with intelligence, style, and a touch of Komi-san’s charm!”_
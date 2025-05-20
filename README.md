# Shouko 🤖

[![Build Status](https://github.com/thetrueheavensequal/Shouko/actions/workflows/ci.yml/badge.svg)](https://github.com/thetrueheavensequal/Shouko/actions)
[![License](https://img.shields.io/github/license/thetrueheavensequal/Shouko)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

A powerful, modular Telegram bot built with [aiogram](https://github.com/aiogram/aiogram) and [Django](https://www.djangoproject.com/), featuring group management, AI chat (Google Gemini), and a web dashboard.

---

## ✨ Features

- **Group Admin Tools:** Ban, mute, promote, and more
- **AI Chat:** Google Gemini integration for smart conversations
- **Event Handling:** Welcome/goodbye messages, logging
- **Web Dashboard:** (Optional) Manage groups and view logs
- **Celery Tasks:** For background jobs and scheduling
- **Dockerized:** Easy deployment with Docker & Compose

---

## 🗂️ Project Structure

```
Shouko/
├── bot/                # Core bot logic (handlers, dispatcher)
├── config/             # Configuration and settings
├── core/               # Django app for DB models & APIs
├── static/             # Frontend assets
├── templates/          # HTML templates
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/thetrueheavensequal/Shouko.git
cd Shouko
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in your secrets (Telegram token, API keys, etc).

### 3. Build and run with Docker

```bash
docker-compose up --build
```

Or run locally:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 4. Start the bot

```bash
python bot/dispatcher.py
```

---

## 🛠️ Configuration

- All settings are in `config/settings/`
- Use `.env` for secrets and environment-specific variables

---

## 🧩 Extending

- Add new bot commands in `bot/handlers/commands.py`
- Add new models in `core/models.py`
- Add Celery tasks in `core/tasks.py`

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

> _“Automate your Telegram groups with intelligence and style!”_
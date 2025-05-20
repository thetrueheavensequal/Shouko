import os
import django
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shouko.settings")
django.setup()

from core.dispatcher import app

if __name__ == "__main__":
    print("Starting Shouko bot...")
    app.run()

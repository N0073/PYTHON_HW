import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

base_url = os.getenv("BASE_URL")
key = os.getenv("KEY")
title = os.getenv("TITLE")
headers = {"Authorization": f"Bearer {key}"}

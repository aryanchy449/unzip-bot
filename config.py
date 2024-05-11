# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    # Mandotory
    APP_ID = int(os.environ.get("API_ID","23080322"))
    API_HASH = os.environ.get("API_HASH","b3611c291bf82d917637d61e4a136535")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6931048916:AAEiwn5cej-PVBw95cqsGskW-BEGx95o4jY")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL","-1002072662567"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER","6214889840"))
    MONGODB_URL = os.environ.get("MONGODB_URL","mongodb+srv://hello:hello@cluster0.s7lxbia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   # GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN","ETgJJ7ITuYFdVBSoamumKXuzKtWuKWYb")
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 1000 # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 120 * 60  # 1 hour 30 minutes (in seconds)

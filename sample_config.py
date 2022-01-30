import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5034247920:AAFxkf4LPKnurMzkvUH5st8QysvQrZTwaZE")
    APP_ID = int(os.environ.get("APP_ID", 10905445))
    API_HASH = os.environ.get("API_HASH", "6a8cead041f2b7640dbb9644dc41ecb0")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001543466659"))

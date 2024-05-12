from dotenv import load_dotenv
from os import getenv, path

load_dotenv() if not path.exists("local.env") else load_dotenv("local.env")


class Config:
    api_id = int(getenv("API_ID", "26477680"))
    api_hash = getenv("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8")
    bot_token = getenv("BOT_TOKEN", "6917853605:AAGicrlrxQ87KAjQol1H-UjlUkWNgtd5ymk")
    log_channel = int(getenv("LOG_CHANNEL", "-1002075430848"))
    fsub_chid = int(getenv("FORCESUB_CHANNEL", "-1002111666674"))
    db_chid = int(getenv("DB_CHANNEL"))
    blacklisted_channel = [int(x) for x in getenv("BLACKLISTED_CHANNEL", "-1002111666674").split(",") if x is not None]
    channel1 = int(getenv("CHANNEL_1", "-1002051332043"))
    channel2 = int(getenv("CHANNEL_2", "-1002068821846"))
    channel3 = int(getenv("CHANNEL_3", "-1002000333870"))


config = Config()

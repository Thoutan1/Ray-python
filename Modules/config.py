import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise EnvironmentError("TOKEN Cannot Be Empty")

    PREFIX = os.getenv("BOT_PREFIX")
    if not PREFIX:
        raise EnvironmentError("PREFIX Cannot Be Empty")

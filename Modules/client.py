import lightbulb
from hikari import Intents, Embed, events, webhooks, errors
from hikari.impl import event_manager_base
# import sys
# sys.path.append('Modules/')
from config import Config

## Starting Bot
bot = lightbulb.Bot(
    token=Config.TOKEN,
    prefix=Config.PREFIX,
    intents=Intents.ALL,
    logs={
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari": {"level": "INFO"},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
            "lightbulb": {"level": "INFO"},
        }
    }
)

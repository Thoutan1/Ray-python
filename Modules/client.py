from lightbulb import Bot
from hikari import Intents, Embed, events, webhooks, errors
from hikari.impl import event_manager_base

from config import Config

class Ray(Bot):
        def __init__(self):

          super().__init__(
            token=Config.TOKEN,
            owner_ids=[776458781239410698],
			insensitive_commands=True,
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

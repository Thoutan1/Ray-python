## Importing Library
import os
import random
import sys
sys.path.append('Modules/')
from client import bot


@bot.command()
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.heartbeat_latency * 1_000:.0f}ms, Your ping {random.randint(0, 100)}")


bot.run()

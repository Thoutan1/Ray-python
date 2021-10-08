from lightbulb import Plugin, command, owner_only
from time import time
import lightbulb
import random
import hikari

class Core(Plugin):

    @command()
    async def ping(self, ctx):
        """Check if I am alive at this present moment"""

        start = time()
        msg = await ctx.respond(
            content = "Pong",
            reply = True
        )
        end = time()
        return await msg.edit(embed = hikari.Embed(
                title = "Ping",
                description = f"**Heartbeat**: {ctx.bot.heartbeat_latency * 1000:,.0f} ms \n**Latency** : {(end - start) * 1000:,.0f} ms",
                color = random.randint(0, 0xffffff)
            )
        )

def load(bot):
    bot.add_plugin(Core())

def unload(bot):
    bot.remove_plugin("Core")

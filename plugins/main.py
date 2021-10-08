from lightbulb import Plugin, command, owner_only
import lightbulb
from time import time
import lightbulb
import random
import hikari
import sys
sys.path.append('Modules/')
import utils

class Core(Plugin):

    @command()
    async def ping(self, ctx):
        """Ping pong"""
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

    @lightbulb.check(lightbulb.owner_only)
    @command(aliases = ['logout'])
    async def shutdown(self, ctx):
        """Shut down the bot"""
        await ctx.respond(embed = Utils.loading_embed())
        await ctx.message.add_reaction("👋")
        return await ctx.bot.close()

def load(bot):
    bot.add_plugin(Core())

def unload(bot):
    bot.remove_plugin("Core")

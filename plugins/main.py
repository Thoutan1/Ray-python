from lightbulb import Plugin, command, owner_only
import lightbulb
import random

class Core(Plugin):

    @command()
    async def ping(self, ctx):
        """Check if I am alive at this present moment"""
        return await ctx.respond(f"Pong! {ctx.bot.heartbeat_latency * 1_000:.0f}ms, Your ping {random.randint(0, 100)}")


def load(bot):
    bot.add_plugin(Core())

def unload(bot):
    bot.remove_plugin("Core")

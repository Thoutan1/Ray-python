# Ray-python

## Setup
```py
pip3 install --no-cache-dir -r requirements.txt
```

## Running
```py
python3 main.py
```

## Example commands
```py
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
          a    description = f"**Heartbeat**: {ctx.bot.heartbeat_latency * 1000:,.0f} ms \n**Latency** : {(end - start) * 1000:,.0f} ms",
              color = random.randint(0, 0xffffff)
          )
      )
```

## Thanks for all.
- Docker setup comming soon

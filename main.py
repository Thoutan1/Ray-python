## Importing Library
from os import listdir
import hikari
import sys
sys.path.append('Modules/')
from client import Ray
bot = Ray()

if __name__ == '__main__':
    for plugin in listdir('plugins'):
        if plugin.endswith('.py'):
            plugin = f"plugins.{plugin.replace('.py', '')}"
            bot.load_extension(plugin)

bot.run()

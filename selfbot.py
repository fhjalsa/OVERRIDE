import discord
from discord.ext import commands
import json
import os
import time
from pretty_help import PrettyHelp
import ctypes

os.system('cls')

logo = """
░█████╗░██╗░░░██╗███████╗██████╗░██████╗░██╗██████╗░███████╗
██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
██║░░██║╚██╗░██╔╝█████╗░░██████╔╝██████╔╝██║██║░░██║█████╗░░
██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗██╔══██╗██║██║░░██║██╔══╝░░
╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██║░░██║██║██████╔╝███████╗
░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝
"""

red = '\033[1;31;48m'
white = '\033[0;37;48m'
blue = '\033[1;34;48m'
cyan = '\033[1;36;40m'
magenta = '\033[1;35;40m'

with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]
delete = config["delete-commands"]
prefix = config["prefix"]

selfbot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True, help_command=None)

if os.path.exists('extensions'):
    extension_count = 0
    for filename in os.listdir('.\\extensions'):
        if filename.endswith('.py'):
            selfbot.load_extension(f'extensions.{filename[:-3]}')
            print(f'{magenta}Loaded {cyan}{filename}{white}')
            extension_count += 1
    time.sleep(2.5)
    os.system('cls')

@selfbot.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f'OverRide || Verison 1.0 || Connected as: {str(selfbot.user)}')
    print(red + logo + white)
    servers = len(selfbot.guilds)
    friends = len(selfbot.user.friends)
    print(f"{magenta}User: {cyan}{str(selfbot.user)}{white}")
    print(f"{magenta}Servers: {cyan}{servers}{white}")
    print(f"{magenta}Friends: {cyan}{friends}{white}")
    print(f"{magenta}Prefix: {cyan}{prefix}{white}")
    print(f"{magenta}Extensions: {cyan}{str(extension_count)}{white}")

@selfbot.event
async def on_command(ctx):
    if delete:
        if ctx.command.name == 'purge':
            pass
        else:
            await ctx.message.delete()

selfbot.run(token, bot=False)
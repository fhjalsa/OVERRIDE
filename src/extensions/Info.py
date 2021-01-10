import discord, webbrowser
from discord.ext import commands

class InfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.url = "https://fhjalsa.github.io"

    @commands.command(name="info",aliases=["Info","Dev","dev"])
    async def info(self, ctx):
        webbrowser.open(self.url)

def setup(client):
    client.add_cog(InfoCommand(client))
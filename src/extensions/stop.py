from discord.ext import commands
import discord

class StopCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stop(self, ctx):
        quit()
    
def setup(client):
    client.add_cog(StopCommand(client))
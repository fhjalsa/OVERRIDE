import discord
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def playing(self, ctx, *, text="OverRide"):
        game = discord.Game(name=text)
        await self.client.change_presence(activity=game)

    @commands.command()
    async def streaming(self, ctx, url, *, text="OverRide"):
        stream = discord.Streaming(name=text, url=url)
        await self.client.change_presence(activity=stream)

    @commands.command()
    async def listening(self, ctx, *, text="OverRide"):
        song = discord.Activity(type=discord.ActivityType.listening, name=text)
        await self.client.change_presence(activity=song)
    
    @commands.command()
    async def watching(self, ctx, *, text="OverRide"):
        video = discord.Activity(type=discord.ActivityType.watching, name=text)
        await self.client.change_presence(activity=video)

    @commands.command()
    async def remove_status(self, ctx):
        await self.client.change_presence(activity=None)
        await ctx.send("Reset Status!")


def setup(client):
    client.add_cog(Status(client))
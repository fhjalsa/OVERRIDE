from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, selfbot):
        self.selfbot = selfbot
    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason=None):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(title=f'Banned {str(member)}', description=f'Reason: `{str(reason)}`', color=0x07f54b) #07f54b
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Seems like I Couldn\'t Ban {str(member)}', color=0xfc030f)
            await ctx.send(embed=embed, delete_after=2.5)

    @commands.command()
    async def kick(self, ctx, member: discord.Member, reason=None):
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f'Kicked {str(member)}', description=f'Reason: `{str(reason)}`', color=0x07f54b) #07f54b
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Seems like I Couldn\'t Kick {str(member)}', color=0xfc030f)
            await ctx.send(embed=embed, delete_after=2.5)
        
    @commands.command()
    async def purge(self, ctx, limit):
        try:
            deleted = await ctx.channel.purge(limit=int(limit))
            embed = discord.Embed(title=f'Deleted `{len(deleted)}` Message(s)', color=0x07f54b)
            await ctx.send(embed=embed, delete_after=2.5)
        except Exception as e:
            embed = discord.Embed(title=f'ERROR! {e} ', color=0xfc030f)
            await ctx.send(embed=embed, delete_after=2.5)

def setup(selfbot):
    selfbot.add_cog(Moderation(selfbot))
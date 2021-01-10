from discord.ext import commands
import discord

green = 0x43B581   #43B581
red = 0xF04947     #F04947

class Lunar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='add-role')
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            embed = discord.Embed(title=f"Added {role.name} for {member.name}", color=green)
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title=f"ERROR: `{e}`", color=red)
            await ctx.send(embed=embed)

    @commands.command(name='remove-role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            embed = discord.Embed(title=f"Removed {role.name} for {member.name}", color=green)
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title=f"ERROR: `{e}`", color=red)
            await ctx.send(embed=embed)

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        try:
            muted_role=discord.utils.get(ctx.guild.roles,name="Muted")
            for role in member.roles:
                try:
                    await member.remove_roles(role)
                except:
                    await ctx.send('`Couldnt remove role(s)`')
            await member.add_roles(muted_role)
            embed = discord.Embed(title=f"Muted {member.name}!", color=green)
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title=f'ERROR: `{e}`', color=red)
            await ctx.send(embed=embed)
        
    @commands.command()
    async def slow(self, ctx, seconds):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!", delete_after=5)

def setup(client):
    client.add_cog(Lunar(client))
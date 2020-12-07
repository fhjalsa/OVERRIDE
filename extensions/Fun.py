from discord.ext import commands
import discord
from datetime import datetime
import time
from pyfiglet import Figlet
import random
import asyncio

purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 0x8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9

class Fun(commands.Cog):
    def __init__(self, selfbot):
        self.selfbot = selfbot
    
    @commands.command()
    async def ascii(self, ctx, *, text: str=None):
        if text is None:
            await ctx.send("`Invalid argument`")
        else:
            f = Figlet(font='Slant')
            j = (f.renderText(text))
            try:
                embed= discord.Embed(color= aqua, description=f"```{j}```",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_footer(text="Made by Fhjalsa")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                try:
                    await ctx.send(f"```{j}```")
                except Exception as e:
                    await ctx.send(f"Error: {e}")

    @commands.command()
    async def dox(self, ctx, user: discord.Member=None):
        emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com"])
        nr = random.choice(range(0,9999))
        ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
        country = random.choice(['Niger', 'Niggeria', "3rd wolrd country", "Africa"])
        if user is None:
            await ctx.send("`Please mention a member`")
        else:
            try:
                embed= discord.Embed(color= green_dark, title=f"Doxing in progress %0",description="Getting his email and address",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
                embed.set_footer(text="Made by Fhjalsa")
                a = await ctx.send(embed=embed)
                await asyncio.sleep(2)
                embed= discord.Embed(color= green_dark, title=f"Doxing in progress %50",description="Getting ip and stuffs",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
                embed.set_footer(text="Made by Fhjalsa")
                await a.edit(embed=embed)
                await asyncio.sleep(2)
                embed= discord.Embed(color= green_dark, title=f"Doxing in progress %100",description="Getting mom credit cards",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
                embed.set_footer(text="Made by Fhjalsa")
                await a.edit(embed=embed)
                await asyncio.sleep(2)
                embed= discord.Embed(color= green_dark, title=f"Dox of {user.name}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
                embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
                embed.add_field(name=f'IP', value=f'{ip}', inline=False)
                embed.add_field(name=f'Country', value=f'{country}', inline=False)
                embed.set_footer(text="Made by Fhjalsa")
                await a.edit(embed=embed)
                await asyncio.sleep(2)
            except discord.HTTPException:
                a = await ctx.send("Doxing in progress %0 - Getting his email and address")
                await asyncio.sleep(2)
                await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
                await asyncio.sleep(2)
                await a.edit(content="Doxing in progress %100 - Getting mom credit cards")
                await asyncio.sleep(2)
                await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")

    @dox.error
    async def dox_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"Error: {error}")
        
    @commands.command()
    async def junknickname(self, ctx):
        try:
            guild = ctx.author.guild
            member = await guild.fetch_member(ctx.author.id)
            name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
            await member.edit(nick=name)
            await ctx.send(f"`nickname now gay`")
        except Exception as e:
            await ctx.send(f"Error: `{e}`")

    @commands.command()
    async def embed(self, ctx, color: discord.Colour=discord.Colour.green(), title='Input text', description=None):
        embed = discord.Embed(title=title, description=description, color=color)
        await ctx.send(embed=embed)

    @commands.command()
    async def everyone(self, ctx, *, text):
        msg = await ctx.send('@everyone')
        await msg.edit(content=text)

def setup(selfbot):
    selfbot.add_cog(Fun(selfbot))
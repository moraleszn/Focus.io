import discord
from discord.ext import commands

# Enable all perms for the bot
intents = discord.Intents.all()

bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def init(ctx:commands.Contex):
    user_name = ctx.author.name 
    await ctx.reply(f"Olá, {user_name}! Tudo bem?")

bot.run("DISCORD_TOKEN")
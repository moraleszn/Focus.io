import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os
from pomodoro import pomodoro
from reminders import remindme
from tasks import addtask, listtasks, downloadtasks


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Enable all perms for the bot
intents = discord.Intents.all()

bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def init(ctx:commands.Context):
    user_name = ctx.author.name
    embed = discord.Embed(
        description=f"Olá, {user_name}! Tudo bem? Estou aqui para ajudar você a gerenciar seus estudos e afazeres. "
                    f"Use o comando `.pomodoro <minutos_pomodoro> <minutos_pausa> <ciclos>` para começar.",
        color=0x57F287  # Verde claro e vivo
    )
    await ctx.reply(embed=embed)



# Importa comandos dos módulos separados
bot.add_command(pomodoro)
bot.add_command(remindme)
bot.add_command(addtask)
bot.add_command(listtasks)
bot.add_command(downloadtasks)

bot.run(DISCORD_TOKEN)
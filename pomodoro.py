from discord.ext import commands
import asyncio

@commands.command()
async def pomodoro(ctx, minutos: int):
    await ctx.reply(f"Pomodoro configurado para {minutos} minutos. Iniciando agora!")
    await asyncio.sleep(minutos * 60)
    await ctx.reply("Tempo do pomodoro acabou! Faça uma pausa.")

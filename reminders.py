from discord.ext import commands
import asyncio

@commands.command()
async def remindme(ctx, tempo: str, *, mensagem: str):
    if tempo.endswith("min"):
        segundos = int(tempo[:-3]) * 60
    elif tempo.endswith("h"):
        segundos = int(tempo[:-1]) * 3600
    else:
        await ctx.reply("Use 'min' para minutos ou 'h' para horas. Exemplo: 15min ou 1h")
        return
    await ctx.reply(f"Lembrete criado! Vou te lembrar de: {mensagem} em {tempo}.")
    await asyncio.sleep(segundos)
    await ctx.reply(f"⏰ Lembrete: {mensagem}")

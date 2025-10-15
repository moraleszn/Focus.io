from discord.ext import commands
import asyncio

# Comando para iniciar um ciclo de pomodoro
@commands.command()
async def pomodoro(ctx, minutos: int):
    """
    Inicia um timer de pomodoro com duração definida pelo usuário.
    Após o tempo, avisa que o ciclo terminou.
    """
    await ctx.reply(f"Pomodoro configurado para {minutos} minutos. Iniciando agora!")  # Informa início
    await asyncio.sleep(minutos * 60)  # Aguarda o tempo do pomodoro
    await ctx.reply("Tempo do pomodoro acabou! Faça uma pausa.")  # Informa fim do ciclo

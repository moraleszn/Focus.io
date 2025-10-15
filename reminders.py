from discord.ext import commands
import asyncio

# Comando para criar um lembrete personalizado
@commands.command()
async def remindme(ctx, tempo: str, *, mensagem: str):
    """
    Agenda um lembrete para o usuário após um tempo definido.
    O tempo pode ser em minutos (ex: 15min) ou horas (ex: 1h).
    """
    # Verifica o formato do tempo e converte para segundos
    if tempo.endswith("min"):
        segundos = int(tempo[:-3]) * 60
    elif tempo.endswith("h"):
        segundos = int(tempo[:-1]) * 3600
    else:
        await ctx.reply("Use 'min' para minutos ou 'h' para horas. Exemplo: 15min ou 1h")
        return
    # Confirma que o lembrete foi criado
    await ctx.reply(f"Lembrete criado! Vou te lembrar de: {mensagem} em {tempo}.")
    # Aguarda o tempo definido
    await asyncio.sleep(segundos)
    # Envia o lembrete ao usuário
    await ctx.reply(f"⏰ Lembrete: {mensagem}")

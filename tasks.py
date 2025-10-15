from discord.ext import commands
import discord

tasks = []

@commands.command()
async def addtask(ctx, *, tarefa: str):
    tasks.append(tarefa)
    await ctx.reply(f"Tarefa adicionada: {tarefa}")

@commands.command()
async def listtasks(ctx):
    if not tasks:
        await ctx.reply("Nenhuma tare\fa adicionada.")
    else:
        msg = '\n'.join([f"{i+1}. {t}" for i, t in enumerate(tasks)])
        await ctx.reply(f"Suas tarefas:\n{msg}")

@commands.command()
async def downloadtasks(ctx):
    await ctx.reply("Baixando tarefas...")
    with open("tasks.txt", "w") as arquivo:
        for i in tasks:
            arquivo.write(i + "\n")
    await ctx.reply(file=discord.File("tasks.txt"))


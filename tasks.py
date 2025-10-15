from discord.ext import commands

tasks = []

@commands.command()
async def addtask(ctx, *, tarefa: str):
    tasks.append(tarefa)
    await ctx.reply(f"Tarefa adicionada: {tarefa}")

@commands.command()
async def listtasks(ctx):
    if not tasks:
        await ctx.reply("Nenhuma tarefa adicionada.")
    else:
        msg = '\n'.join([f"{i+1}. {t}" for i, t in enumerate(tasks)])
        await ctx.reply(f"Suas tarefas:\n{msg}")

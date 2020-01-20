from os import getenv
from discord.ext import commands

TOKEN = getenv('DISCORD_TOKEN', '')

bot = commands.Bot(command_prefix='/')


@bot.command(name='start')
async def start_mc_server(ctx):
    await ctx.send(f'Minecraftサーバーを起動中です。')


bot.run(TOKEN)

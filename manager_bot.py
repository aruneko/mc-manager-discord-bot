from os import getenv

from discord.ext import commands
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

TOKEN = getenv('DISCORD_TOKEN', '')
PROJECT_ID = getenv('GCP_PROJECT_ID', '')
ZONE = getenv('GCP_ZONE', 'asia-northeast1-b')
RESOURCE_ID = getenv('GCP_RESOURCE_ID', '')
CREDENTIAL_JSON = getenv('GCP_CREDENTIAL_JSON', '')

bot = commands.Bot(command_prefix='/')


@bot.command(name='start')
async def start_mc_server(ctx):
    await ctx.send('Minecraftサーバーを起動中です。')
    credential = Credentials.from_service_account_file(CREDENTIAL_JSON)
    resource = discovery.build('compute', 'v1', credentials=credential)
    request = resource.instances().start(project=PROJECT_ID, zone=ZONE, instance=RESOURCE_ID)
    response = request.execute()
    await ctx.send('Minecraftサーバーを起動しました')


@bot.command(name='stop')
async def stop_mc_server(ctx):
    await ctx.send(f'Minecraftサーバーを停止中です。')
    credential = Credentials.from_service_account_file(CREDENTIAL_JSON)
    resource = discovery.build('compute', 'v1', credentials=credential)
    request = resource.instances().stop(project=PROJECT_ID, zone=ZONE, instance=RESOURCE_ID)
    response = request.execute()
    await ctx.send(f'Minecraftサーバーを停止しました。')


bot.run(TOKEN)

import discord, os, random, asyncio, win10toast
from discord.ext import commands, tasks
from environs import Env



intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = ',', intents=intents)



env = Env()
env.read_env()

TOKEN = env.str("DSBOT_TOKEN")
GUILD = ('πππππππππ πππππ')




@client.event
async def on_ready():

	toaster = win10toast.ToastNotifier()
	toaster.show_toast('WANTIAGOO MAIN BOT', 'is connected')

	guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
		)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, ΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΠ΅Π»Ρ Π½Π΅ Π½Π°ΠΉΠ΄Π΅Π½!**', color=0x0c0c0c))


initial_extensions = []

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		initial_extensions.append(f'cogs.{filename[:-3]}')

print(initial_extensions)
if __name__ == '__main__':
	for extension in initial_extensions:
		client.load_extension(extension)


client.run(TOKEN)
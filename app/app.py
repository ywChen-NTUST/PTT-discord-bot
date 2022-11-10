import nextcord
from nextcord.ext import commands

from cogs.modules.params import TOKEN


intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}.")

if __name__ == "__main__":
	cogs = ["PTT", "Board", "Util"]
	for cog in cogs:
		bot.load_extension(f"cogs.{cog}")

	bot.run(TOKEN)
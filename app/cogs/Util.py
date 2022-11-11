import time

import requests
import nextcord
from nextcord.ext import commands

from .modules.params import GUILD_ID
from .modules.description import DESCRIPTION
from .modules.formatter import make_help_embed


class Util(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		
	@nextcord.slash_command(description=DESCRIPTION["Util"]["ping"]["describe"])
	async def ping(self, interaction: nextcord.Interaction) -> None:
		latency = round(self.bot.latency * 1000, 1)
		await interaction.response.send_message(f"pong!\nlatency: {latency} ms")
	
	@nextcord.slash_command(description=DESCRIPTION["Util"]["ping_ptt"]["describe"])
	async def ping_ptt(self, interaction: nextcord.Interaction) -> None:
		t0 = time.time()
		res = requests.get("https://www.ptt.cc/bbs/")
		t1 = time.time()
		latency = round((t1 - t0) * 1000, 1)
		status_code = res.status_code
		await interaction.response.send_message(f"pong!\nstatus code: {status_code}\nlatency: {latency} ms")

	@nextcord.slash_command(description=DESCRIPTION["Util"]["help"]["describe"])
	async def help(self, interaction: nextcord.Interaction) -> None:
		embed = make_help_embed()
		await interaction.response.send_message(embed=embed)
	
	@nextcord.slash_command(guild_ids=[GUILD_ID], description=DESCRIPTION["Util"]["sync"]["describe"])
	async def sync(self, interaction: nextcord.Interaction) -> None:
		await self.bot.sync_application_commands()
		await interaction.response.send_message("sync successfully")

def setup(bot: commands.Bot) -> None:
	bot.add_cog(Util(bot))
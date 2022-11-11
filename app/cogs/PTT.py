import requests
import nextcord
from nextcord.ext import commands

from .modules.description import DESCRIPTION
from .modules.parser import parse_ptt_mainpage
from .modules.formatter import make_ptt_top_embed


class PTT(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
    
	@nextcord.slash_command()
	async def ptt(interaction: nextcord.Interaction):
		"""
		This will never get called since it has subcommands.
		"""
		pass
		
	@ptt.subcommand(description=DESCRIPTION["PTT"]["top"]["describe"])
	async def top(self, interaction: nextcord.Interaction, limit: int=3) -> None:
		res = requests.get("https://www.ptt.cc/bbs/index.html")
		if(res.status_code != 200):
			await interaction.response.send_message("failed to connect PTT!")
		else:
			parsed = parse_ptt_mainpage(res.text)
			restricted = parsed[:limit]
			embed = make_ptt_top_embed(restricted)
			await interaction.response.send_message(embed=embed)
	
	@ptt.subcommand(description=DESCRIPTION["PTT"]["users"]["describe"])
	async def users(self, interaction: nextcord.Interaction) -> None:
		res = requests.get("https://www.ptt.cc/bbs/index.html")
		if(res.status_code != 200):
			await interaction.response.send_message("failed to connect PTT!")
		else:
			parsed = parse_ptt_mainpage(res.text)
			users = sum([p["users"] for p in parsed])
			await interaction.response.send_message(f"there are {users} users in PTT for now")

def setup(bot: commands.Bot) -> None:
	bot.add_cog(PTT(bot))
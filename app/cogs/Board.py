import requests
import nextcord
from nextcord.ext import commands

from .modules.params import GUILD_ID
from .modules.description import DESCRIPTION
from .modules.parser import parse_ptt_boardpage
from .modules.formatter import make_article_embed


class Board(commands.Cog):
	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
    
	@nextcord.slash_command(guild_ids=[GUILD_ID])
	async def board(interaction: nextcord.Interaction):
		"""
		This will never get called since it has subcommands.
		"""
		pass
		
	@board.subcommand(description=DESCRIPTION["Board"]["latest"]["describe"])
	async def latest(self, interaction: nextcord.Interaction, board: str, limit: int=3) -> None:
		res = requests.get(f"https://www.ptt.cc/bbs/{ board }/index.html", cookies={"over18":"1"})
		if(res.status_code != 200):
			res = requests.get("https://www.ptt.cc/bbs/index.html")
			if(res.status_code != 200):
				await interaction.response.send_message("failed to connect PTT!")
			else:
				await interaction.response.send_message(f"Board: { board } not found!")
		else:
			parsed, lastpage = parse_ptt_boardpage(res.text)

			# if there is no enough data in current page
			while(len(parsed) < limit and lastpage != None):
				res = requests.get(lastpage, cookies={"over18":"1"})
				parsed2, lastpage = parse_ptt_boardpage(res.text)
				parsed += parsed2
			
			restricted = parsed[:limit]
			embed = make_article_embed(restricted)
			await interaction.response.send_message(embed=embed)
	
	@board.subcommand(description=DESCRIPTION["Board"]["search"]["describe"])
	async def search(self, interaction: nextcord.Interaction, 
		board: str, article:str=None, author:str=None, limit: int=3
	) -> None:
		if(article == None and author == None):
			await interaction.response.send_message("No author nor article!")
			return
		
		query = ""
		if(article != None):
			query += article
		if(author != None):
			if(query != ""):
				query += "+"
			query += "author:" + author
		
		res = requests.get(f"https://www.ptt.cc/bbs/{ board }/search?q={ query }", cookies={"over18":"1"})
		if(res.status_code != 200):
			res = requests.get("https://www.ptt.cc/bbs/index.html")
			if(res.status_code != 200):
				await interaction.response.send_message("failed to connect PTT!")
			else:
				await interaction.response.send_message(f"Board: { board } not found!")
		else:
			parsed, lastpage = parse_ptt_boardpage(res.text, new_first=False)

			# if there is no enough data in current page
			while(len(parsed) < limit and lastpage != None):
				res = requests.get(lastpage, cookies={"over18":"1"})
				parsed2, lastpage = parse_ptt_boardpage(res.text, new_first=False)
				parsed += parsed2
			
			restricted = parsed[:limit]
			embed = make_article_embed(restricted)
			await interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot) -> None:
	bot.add_cog(Board(bot))
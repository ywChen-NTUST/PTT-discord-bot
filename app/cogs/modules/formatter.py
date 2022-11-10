import nextcord

from .description import DESCRIPTION


def make_help_embed() -> nextcord.Embed:
	"""
	make embed for `/help` in Util cog

	Input: None
	Output: nextcord.Embed
	"""
	embed = nextcord.Embed(title = "Help")
	for category, commands in DESCRIPTION.items():
		content = ""
		for command_describe in commands.values():
			content += f'`{ command_describe["command"] }\n`'
			content += f'➜ { command_describe["describe"] }\n'
		embed.add_field(name=category, value=content, inline=False)
	return embed

def make_ptt_top_embed(data: list) -> nextcord.Embed:
	"""
	make embed for `/ptt top` in PTT cog

	Input: [
		{
			"url": board url (str)
			"name": board name (str)
			"users": board online users (int)
			"category": board category (str)
			"describe": board describe (str)
		}, {...}, ...
	]
	Output: nextcord.Embed
	"""
	embed = nextcord.Embed(title = "Hot Boards")
	for d in data:
		content = f'> 在線人數: { d["users"] }\n'
		content += f'> { d["describe"] }\n'
		content += f'> [進入頁面]({ d["url"] })\n'
		embed.add_field(name=d["name"], value=content, inline=False)
	return embed

def make_article_embed(data: list) -> nextcord.Embed:
	"""
	make embed for `/ptt top` in PTT cog

	Input: [
		{
			"url": article url (str)
			"title": article title (str)
			"author": article author (str)
			"score": article score (str)
		}, {...}, ...
	]
	Output: nextcord.Embed
	"""
	content = ""
	for d in data:
		content += f'{d["score"]}　[{d["title"]}]({d["url"]}) (作者: {d["author"]})\n'

	embed = nextcord.Embed(title = "Latest Article", description = content)
	return embed
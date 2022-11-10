from bs4 import BeautifulSoup


def parse_ptt_mainpage(text: str) -> list:
	"""
	parse HTML in ptt mainpage to list of data

	Input: HTML text
	Output: [
		{
			"url": board url (str)
			"name": board name (str)
			"users": board online users (int)
			"category": board category (str)
			"describe": board describe (str)
		}, {...}, ...
	]
	"""
	soup = BeautifulSoup(text, "html.parser")
	boards = soup.findAll("div", {"class": "b-ent"})

	parsed = []
	for board in boards:
		boardData = dict()
		boardData["url"] = "https://www.ptt.cc" + board.find("a").get("href")
		boardData["name"] = board.find("div", {"class":"board-name"}).text
		boardData["users"] = int(board.find('span').text)
		boardData["category"] = board.find("div", {"class":"board-class"}).text
		boardData["describe"] = board.find("div", {"class":"board-title"}).text
		parsed.append(boardData)

	return parsed

def parse_ptt_boardpage(text: str, new_first: bool = True) -> tuple:
	"""
	parse HTML in ptt board page to list of data and lastpage url

	Input: HTML text
	Output: (
		[{
			"url": article url (str)
			"title": article title (str)
			"author": article author (str)
			"score": article score (str)
		}, {...}, ...], new_first = True
		lastpage url (str)
	)
	"""
	soup = BeautifulSoup(text, "html.parser")

	# get previous page url
	lastpage = soup.find("div", {"class": "btn-group-paging"}).findAll("a", {"class": "btn"})[1].get("href")
	if(lastpage is not None):
		lastpage = "https://www.ptt.cc" + lastpage
	
	announcementSep = soup.find("div", {"class": "r-list-sep"})
	if(announcementSep is not None):
		# has announcement section
		# reference: https://stackoverflow.com/questions/47724241/beautifulsoup-find-all-tags-before-stopping-condition-is-met
		articles = announcementSep.find_all_previous("div", {"class": "r-ent"})
		if(not new_first):
			articles.reverse()
	else:
		articles = soup.findAll("div", {"class": "r-ent"})
		if(new_first):
			articles.reverse()

	parsed = []
	for article in articles:
		if (article.find("a") is None):
			# had been deleted or reported
			continue

		articleData = dict()
		articleData["url"] = "https://www.ptt.cc" + article.find("a").get("href")
		articleData["title"] = article.find("a").text
		articleData["author"] = article.find("div", {"class": "author"}).text
		score = article.find("div", {"class": "nrec"}).find("span")
		articleData["score"] = 0 if score is None else score.text
		parsed.append(articleData)

	return parsed, lastpage
import feedparser

def extractRss(url):
	tups = []
	feed = feedparser.parse(url)
	for entry in feed.entries:
		tups.append((entry.link, entry.published))
	return tups

def sortTuple(tup):
	tup.sort(key = lambda x: x[1], reverse=True)
	return tup

def getLinks(tupList):
	return [x[0] for x in tupList]

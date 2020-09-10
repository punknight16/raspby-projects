import json

def getFromFile():
	f = open("local_file.json")
	jsonl_content = f.read()
	result = [json.loads(jline) for jline in jsonl_content.splitlines()]
	return result

#def getFromFile():
#	arr = []
#	f = open("local_file.json")
#	line = f.readline()
#	while line:
#		print(type(line))
#		data = json.loads(line),
#		print(type(data))
#		arr.append(data),
#		line = f.readline()
#	f.close()
#	return arr

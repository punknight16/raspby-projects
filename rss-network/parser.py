import yaml

def parseYaml():
	with open("rss-urls.yml", 'r') as stream:
		return yaml.safe_load(stream)

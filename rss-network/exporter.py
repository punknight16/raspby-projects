import yaml

def exportYaml(stack):
	print(stack)
	with open('links.yml', 'w') as f:
		data = yaml.dump(stack, f)



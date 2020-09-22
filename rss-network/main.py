import parser
import extractor
import transformer
import exporter

def main():
	stack = []
	urls = parser.parseYaml()
	for url in urls:
		tups = extractor.extractRss(url)
		stack = stack + tups
	stack = transformer.sortTuple(stack)
	links = transformer.getLinks(stack)
	exporter.exportYaml(links)

if __name__ == "__main__":
	main()

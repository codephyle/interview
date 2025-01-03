import re

def file_read(name):
	pattern = r'[Ee]rror'
	pattern = re.compile(pattern)

	with open(name) as f:
		for line in f:
			if pattern.search(line):
				print(line, end="")

file_read("sre.md")

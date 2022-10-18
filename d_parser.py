import json

d = {}

with open("dictionary.txt", 'r') as inFile:
	for row in inFile:
		parts = row.split('-')

		try:
			d[parts[0]] = parts[1]
		except:
			d[parts[0]] = ''

with open("dictionary.json", "w") as outFile:
	json.dump(d, outFile)
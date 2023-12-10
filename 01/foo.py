#!/usr/bin/env python3

spellings = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]

def parser(line):
	digits_out = []
	i = 0
	while i < len(line):
	    if line[i].isdigit():
	    	digits_out.append(line[i])
	    for sp in spellings:
	    	if line[i:i+len(sp[0])] == sp[0]:
	    		digits_out.append(sp[1])
	    i += 1
	    continue
	str_out = digits_out[0] + digits_out[-1]
	int_out = int(str_out)
	return int_out

if __name__ == "__main__":
	with open("data.txt", "r") as f:
		contents = f.read()
	lines = contents.split("\n")
	results = []
	for line in lines:
		results.append(parser(line))
	print(sum(results))

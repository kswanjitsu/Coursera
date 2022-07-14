import re

fname = "graded_regex.txt"
fhand = open(fname, "r").read()
x = re.findall('[0-9]+',fhand)
y = sum([int(i) for i in x])
print(y)
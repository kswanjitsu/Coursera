"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution
 by hour of the day for each of the messages. You can pull the hour out from the 'From ' line
  by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

filename = input("Enter file:")

if len(filename) < 1:
    filename = "mbox-short.txt"

handle = open(filename)

counts = {}

for line in handle:
    if line.startswith('From '):
        words = line.rstrip().split()
        for word in words:
            hours = words[5]
            hour = hours.split(':')[0]

        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key,value in counts.items():
    newtup = (key,value)
    lst.append(newtup)

print(sorted(lst))
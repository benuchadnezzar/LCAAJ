import csv
import re

# creates a .csv file into which our results will go
outputFile = open("responses-and-notes-separated.csv", "w", newline="")

# creates the object that will take our data and write it to our .csv
outputWriter = csv.writer(outputFile)

# list of all the regex terms we want to check for
# double check the regex (^\* | \*$) because the * character in the 
# LCAAJ's editors' notes had an ambiguous explanation, and this might
# be an incorrect regex. this may also correspond to a star of david
# in the data, which will not be a * in the OCRed product.
# also note that for the regexes that denote parts of speech (such as 
# QADJ, QVB, and QNOUN) a complete list may not have been provided,
# and others may need to be added.
notation = r"(?:(?:(?:\$|\)[+=-]?|\*|^\+\$?|-\$?|[O0]\b|=))|(?:(?:\$|\)[+=-]?|\*|\+\$?|-|=)$)|Q[BHKNPRSTUVW]\b|(?:(?:[+-]BUT|Q(?:E[DT]|GL|[IQ]))\b)|(?:\b(?:C(?:LN|M)|SC|XX)\b)|\|{2}|\.{3}|/[^/]+/|\(/\d*|\(\d*|\(\$\d*|\(\(|-\$|\u2721|(?:DRWG|EQ|MIS(?:PMP|TD)|OVRPMP|Q(?:-(?:AP|[KTUW])|A(?:DJ|MER|NG|P)|BF|CF|DG|E(?:D[NS]|LSW|M|NG|TC)|F(?:/Y|R)|G(?:ERM|L[EY])|HU(?:M|NG)|I(?:GL|NF)|L(?:AT|IT)|M(?:/Y|EMX)|N(?:EX|OUN|[NPT])|O(?:F|OF|TW)|POL|R(?:R|TR|U(?:M|SS))|S(?:MT|YN)|T[AF]|UU|V[BL]|YID|Z[TZ]|aQ)))"

# list of lists, two items each, that will become columns according to the .csv file
notesSeparate = []

# make sure you take out x.doctype and put in the actual file name once
# we have it.
with open("x.doctype") as f:
	data = f.readlines()

# goes through text line by line, separates regexes from surrounding text,
# and appends those to a list
for line in data:
	newRow = []
	notes = str.strip(", ".join(re.findall(notation, line, re.X)))
	response = str.strip(str(re.sub(notation, "", line, re.X)))
	newRow.append(response)
	newRow.append(notes)
	notesSeparate.append(newRow)

for item in notesSeparate:
	outputWriter.writerow(item)

outputFile.close()
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
notation = [r"(^\+ | \+$)", r"(^- | -$)", r"( \+ BUT\b)", r"( - BUT\b)", 
r"(^\$ | \$$)", r"(^\+\$ | \+\$$)", r"(^-\$ | -\$)", r"(DRWG)", r"(QB\b)", 
r"(QT\b)", r"(QBF)", r"(QTF)", r"(QFR)", r"(^= | =$)", r"(Q a Q)", r"(QP\b)", 
r"(QM/Y)", r"(QF/Y)", r"(^\* | \*$)", r"(QU\b)", r"(Q-U)", r"(QUU)", r"(QR\b)", 
r"(QRR)", r"(QH\b)", r"(QS\b)", r"(QW\b)", r"(Q-W)", r"(QAP)", r"(Q-AP)", r"(QN\b)", 
r"(QNN)", r"(QOF)", r"(QOOF)", r"(QK\b)", r"(Q-K)", r"(QLIT)", r"(QV\b)", r"(QEM)", 
r"(QVL)", r"(QDG)", r"(QAMER)", r"(QHUM)", r"(QELSW)", r"(QRTR)", r"(QSMT)", r"(QOTW)", 
r"(QNEX)", r"(QET\b)", r"(QPOL)", r"(QRUS)", r"(QRUM)", r"(QHUNG)", r"(QGERM)", r"(QSYN)", 
r"(QGL\b)", r"(QGLY)", r"(QYID)", r"(QGLE)", r"(QENG)", r"(QI GL)", r"(QANG)", r"(QI\b)", 
r"(^\) | \)$)", r"(^\)\+ | \)\+$)", r"(^\)- | \)-$)", r"(^\)= | \)=$)", 
r"(EQ)", r"(\|\|)", r"(QCF)", r"(QZZ)", r"(QZT)", r"(\.\.\.{1})", r"(QETC)", r"(QVB)", 
r"(QADJ)", r"(QINF)", r"(QNOUN)", r"(/[^/]+/)", r"(\b/)", r"(\bCM\b)", r"(\bCLN\b)", 
r"(\bSC\b)", r"(\bXX\b)", r"(QQ\b)", r"(^0\b)", r"(^O\b)", r"(QNT)", r"(Q-T)", r"(QLAT)", 
r"(QTA)", r"(QNP)", r"(QMEMX)", r"(\u2721)"]

# re.split() in the loop below will separate each regex from the other
# text on that line and place those two pieces into a list.
# notesSeparate is a list of those lists.
notesSeparate = []

# make sure you take out x.doctype and put in the actual file name once
# we have it.
with open("x.doctype") as f:
	data = f.readlines()

# goes through text line by line and separates out regexes
for line in data:
	for item in notation:
		i = 0
		while i < len(notation):
			if re.search(notation[i]):
				notesSeparate.add(re.split(notation[i], line))
				i += 1
			else:
				i += 1

for item in notesSeparate:
	outputWriter.writerow(item)

outputFile.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import enchant
import regex as re

# creates a .csv file into which our results will go
outputFile = open("responses-and-notes-separated.csv", "w")

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
notation = r"(?:(?:(?:(?:(?:\()?\$(?:\d*)?)|\)[+=-]?|\*|^\+\$?|-\$?|[O0]\b|=))|(?:(?:\$|\)[+=-]?|\*|\+\$?|-|=)$)|Q[BHKNPRSTUVW]\b|(?:(?:[+-]BUT|Q(?:E[DT]|GL|[IQ]))\b)|(?:\b(?:C(?:LN|M)|SC|XX)\b)|\|{2}|\.{3}|/[^/]+/|\(/\d*|\(\d*|\(\$\d*|\(\(|-\$|\u2721|(?:DRWG|EQ|MIS(?:PMP|TD)|OVRPMP|Q(?:-(?:AP|[KTUW])|A(?:DJ|MER|NG|P)|BF|CF|DG|E(?:D[NS]|LSW|M|NG|TC)|F(?:(?:/Y)?|R)|G(?:ERM|L[EY])|HU(?:M|NG)|I(?:GL|NF)|L(?:AT|IT)|M(?:(?:/Y)?|EMX)|N(?:EX|OUN|[NPT])|O(?:F|OF|TW)|POL|R(?:R|TR|U(?:M|SS))|S(?:MT|YN)|T[AF]|UU|V[BL]|YID|Z[TZ]|aQ)))"

# import English dictionary to check for English words
d = enchant.Dict("en_US")
d.add("DIFF")
d.add("DONT")
d.remove("FUN")
d.remove("A")

# list of lists, two items each, that will become columns according to the .csv file
notesSeparate = []

# converts responses to International Phonetic Alphabet
def responsesIPA(response):
	global IPA
	IPA = response.lower()
	IPA = re.sub("\B\\\B", "", IPA)
	IPA = re.sub("3", "ə", IPA)
	IPA = re.sub("1", "ɨ̞", IPA)
	IPA = re.sub("6", "ʌ", IPA)
	IPA = re.sub("(?<=[mnptkbdgfsxhvzclrjw])\.", "ː", IPA)
	IPA = re.sub("\.{1}", "", IPA)
	IPA = re.sub("\.\.", "ː", IPA)
	IPA = re.sub("94", "̆", IPA)
	IPA = re.sub("95", "-", IPA)
	IPA = re.sub("(?<![szcptkbdgfv])\+", "̃", IPA)
	IPA = re.sub("e[^j](4){0,1}", "ɛ", IPA)
	IPA = re.sub("e44", "æ", IPA)
	IPA = re.sub("i4", "e", IPA)
	IPA = re.sub("o[^j](4){0,1}", "æ", IPA)
	IPA = re.sub("o44", "ɒ", IPA)
	IPA = re.sub("ɛ5", "e", IPA)
	IPA = re.sub("a7", "ɑ", IPA)
	IPA = re.sub("a57", "ɐ", IPA)
	IPA = re.sub("a58", "a", IPA)
	IPA = re.sub("o5[^78]", "u", IPA)
	IPA = re.sub("u5[^78]", "o", IPA)
	IPA = re.sub("ɛ7", "ʌ", IPA)
	IPA = re.sub("e7", "ɤ", IPA)
	IPA = re.sub("i7", "ɯ", IPA)
	IPA = re.sub("ɔ8", "œ", IPA)
	IPA = re.sub("o8", "ø", IPA)
	IPA = re.sub("u", "y", IPA)
	IPA = re.sub("92", "ʔ", IPA)
	IPA = re.sub("(?<=[mnptkbdgfsxhvzclrjw]((2(-)?)?|(7(8)?)?|(8)?)?[+-]?),", "̩", IPA)
	IPA = re.sub("s\+", "ʃ", IPA)
	IPA = re.sub("z\+", "ʒ", IPA)
	IPA = re.sub("c\+", "tʃ", IPA)
	IPA = re.sub("(?<=[ptkbdgfv])\+", "n̩", IPA)
	IPA = re.sub("(?<=([mnptkbdgfsxhvzclrjw]|ʔ|̩))-", "", IPA)
	IPA = re.sub("2-", "", IPA)
	IPA = re.sub("(?<=[mnbdgvzlrjw])2", "̥", IPA)
	IPA = re.sub("(?<=[ptkfsxhc])2", "̬", IPA)
	IPA = re.sub("78", "", IPA)
	IPA = re.sub("(?<=([mnptkbdgfxhvlrjw]|ʔ|̩))7", "ˠ", IPA)
	IPA = re.sub("(?<=([mnptkbdgfsxhvzclrjw]|ʔ|̩))8", "ʲ", IPA)
	IPA = re.sub("c", "ts", IPA)

# copies responses from IPA to YIVO English spelling
def responsesYIVOEng(IPA):
	global YIVO
	YIVO = IPA
	YIVO = re.sub("ə", "e", YIVO)
	YIVO = re.sub("ɨ̞", "i", YIVO)
	YIVO = re.sub("ʌ", "a", YIVO)
	YIVO = re.sub("ː", "", YIVO)
	YIVO = re.sub("̆", "", YIVO)
	YIVO = re.sub("-", "", YIVO)
	YIVO = re.sub("̃", "", YIVO)
	YIVO = re.sub("ɛ", "e", YIVO)
	YIVO = re.sub("æ", "a", YIVO)
	YIVO = re.sub("ɔ", "o", YIVO)
	YIVO = re.sub("ɒ", "o", YIVO)
	YIVO = re.sub("ɑ", "a", YIVO)
	YIVO = re.sub("ɐ", "a", YIVO)
	YIVO = re.sub("ʌ", "a", YIVO)
	YIVO = re.sub("ɤ", "o", YIVO)
	YIVO = re.sub("ɯ", "u", YIVO)
	YIVO = re.sub("œ", "e", YIVO)
	YIVO = re.sub("ø", "e", YIVO)
	YIVO = re.sub("ʔ", "", YIVO)
	YIVO = re.sub("̩", "", YIVO)
	YIVO = re.sub("n̩", "n", YIVO)
	YIVO = re.sub("̥", "", YIVO)
	YIVO = re.sub("̬", "", YIVO)
	YIVO = re.sub("ˠ", "", YIVO)
	YIVO = re.sub("ʲ", "", YIVO)
	YIVO = re.sub("ʃ", "sh", YIVO)

# make sure you take out test.txt and put in the actual file name once
# we have it.
with open("test.txt") as f:
	data = f.readlines()

# goes through text line by line, separates regexes from surrounding text,
# and appends those to a list. also joins all english words to notes string.
for line in data:
	newRow = []
	engWords = ""
	for word in line.split():
		if d.check(word):
			engWords += " " + word
			line = line.replace(word, "")
	notes = ", ".join(re.findall(notation, line)) + engWords
	response = str.strip(str(re.sub(notation, "", line)))
	responsesIPA(response)
	responsesYIVOEng(IPA)
	newRow.append(response)
	newRow.append(IPA)
	newRow.append(YIVO)
	newRow.append(notes)
	notesSeparate.append(newRow)

for item in notesSeparate:
	outputWriter.writerow(item)

outputFile.close()
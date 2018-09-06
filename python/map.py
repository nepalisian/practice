#!/usr/bin/python

fd = open("textfile" , "r")
content = fd.read()

word_to_count = {}

list_words = content.strip().replace(" ", "")

for i in list_words:
    if i in word_to_count.keys():
		word_to_count[i] = word_to_count[i] + 1
    else:
		word_to_count[i] = 1

print(word_to_count)

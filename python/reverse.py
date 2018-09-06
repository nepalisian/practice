#!/usr/bin/python

input = raw_input()
a = input.split(",")
b = []

length = len(a) 
index = length - 1

while (index >= 0):
	b.append(a[index])
	index = index - 1	

print("a: %s" % a)
print("b: %s" % b)


#!/usr/bin/python

a = [ 3,5,4,1,2 ]
b = a[:]

o = []


def sort(a):
	for j in b:
		min = 10000000
		for i in a:
			if i < min:
				min = i
		o.append(min)
		a.remove(min)
	return o

if __name__ == "__main__":
	print(sort(a))


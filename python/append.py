#!/usr/bin/python


a = [1,2,3,4,5]

a.append(0)


length = len(a)

b = [0] * length

index = 0 - length

while (index < 0):
	b[index+1] = a[index]
	index = index + 1

print("a: %s", a)
print("b: %s", b)

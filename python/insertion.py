#!/usr/bin/python

a = [5, 2, 4, 1, 7, 3, 6]

def swap(a, x, y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp
	return a

def insertion(array):
	index = 1
	while index < len(array):
		tmp_index = index
		while tmp_index > 0 and array[tmp_index-1] > array[tmp_index]:
			array = swap(array, tmp_index, tmp_index-1)
			tmp_index = tmp_index - 1
		index = index + 1
		print(array)
	return array
	
if __name__ == "__main__":
	a = insertion(a)
	print(a)

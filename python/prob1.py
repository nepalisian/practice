#!/usr/bin/python

file_content = []

def largestN(array, num):
	return array[:num]

def process(filepath):
	fd = open(filepath, "r")
	for line in fd:
		file_content.append(int(line.strip()))
	return sorted(file_content, reverse=True)

def main():
	print("Enter the file path:")
	filepath = str(raw_input().strip())
	print("Enter the number:")
	numbers = int(raw_input().strip())
	sorted_array = process(filepath)
	topN = largestN(sorted_array, numbers)
	print(topN)

if __name__ == "__main__":
	main()

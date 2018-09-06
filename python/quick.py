#!/usr/bin/python

a = [10, 7, 9, 15, 12, 8, 3, 2, 6, 11]

def quicksort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quicksort(array, low, index - 1)
        quicksort(array, index + 1, high)

def swap(A, x, y):
    if len(A) < x + 1 or len(A) < y + 1:
        return A
    else:
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
        return A

def partition(array, low, high):
    pivot = array[high]
    i = low
    j = low
    while j < high:
        if array[j] < pivot:
            swap(array, i, j)
            i = i + 1
        j = j + 1
    swap(array, i, high)
    return i


def main():
    length = len(a)
    low = 0
    high = length - 1
    quicksort(a, low, high)
    print(a)


if __name__ == "__main__":
    main()
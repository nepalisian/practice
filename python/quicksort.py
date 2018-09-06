#!/usr/bin/python


def swap(arr, x, y):
    try:
        tmp = arr[x]
        arr[x] = arr[y]
        arr[y] = tmp
    except Exception as e:
        print("Caught IndexError")
    return arr


def sort(arr, low, high):
    try:
        if low < high:
            index = partition(arr, low, high)
            sort(arr, low, index-1)
            sort(arr, index+1, high)
    except Exception as e:
        print("Caught Exception")

def partition(arr, low, high):
    i = low
    j = low
    pivot = arr[high]
    while j < high:
        if arr[j] < pivot:
            swap(arr, i, j)
            i = i + 1
        j = j + 1
    swap(arr, i, high)
    return i


def convert(s):
    a = s.strip().split(",")
    return a


def positive(num):
    if num > 0:
        return True
    else:
        return False

def main():
    while True:
        swap([], 0, 1)

if __name__ == "__main__":
    main()
#!/usr/bin/python


a = [7, 2, 10, 5, 4, 8, 1]

def merge_sort(arr, low, high):
    print("%s %s %s" % (arr, low, high))
    if low < high:
        middle = (low + high)/2
        merge_sort(arr, low, middle)
        merge_sort(arr, middle+1, high)
        merge(arr, low, middle, high)


def merge(arr, low, middle, high):
    left_arr = arr[low:middle+1]
    right_arr = arr[middle+1:high+1]


    i = 0
    j = 0
    k = low

    len_left_arr = len(left_arr)
    len_right_arr = len(right_arr)

    while i < len_left_arr and j < len_right_arr:

        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
        k = k + 1

    while i < len_left_arr:
        arr[k] = left_arr[i]
        i = i + 1
        k = k + 1

    while j < len_right_arr:
        arr[k] = right_arr[j]
        j = j + 1
        k = k + 1


def main():
    print(a)
    merge_sort(a, 0, len(a)-1)
    print(a)


if __name__ == "__main__":
    main()


a = [10, 4, 7, 2, 19, 5]

sorted_a = []


def linearsearch(arr, num):
    found = False
    for i in arr:
        if i == num:
            found = True
            break
    return found


def iterative_binarysearch(arr, num):
    found = False
    first = 0
    last = len(arr) - 1

    while first <= last and found == False:
        mid = (first + last)/2

        if num == arr[mid]:
            found = True
        else:
            if num < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def recursive_bs(arr, num):
    found = False
    first = 0
    last = len(arr) - 1
    mid = (first + last) / 2

    if len(arr) == 0:
        return found

    if first == last:
        if num == arr[mid]:
            found = True
            return found
        else:
            return found

    if num == arr[mid]:
        found = True
        return found
    else:
        if num < arr[mid]:
            found = recursive_bs(arr[:mid], num)
        else:
            found = recursive_bs(arr[mid+1:], num)
    return found


def main():
    #print linearsearch(a, 5)
    print recursive_bs(sorted_a, 18)


if __name__ == "__main__":
    main()
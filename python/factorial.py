#!/usr/bin/python


def factorial(num):
    if num == 1:
        return 1
    else:
        fact = num * factorial(num-1)
    return fact

def main():
    print("Enter the number:")
    number = int(raw_input())
    result = factorial(number)
    print(result)

if __name__ == "__main__":
    main()


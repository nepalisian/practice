def better_divide(func):
    def inner_func(a, b):
        if b == 0:
            print("Oops, can't divide by zero")
            return
        else:
            return func(a, b)
    return inner_func


@better_divide
def divide(a, b):
    return a/b


if __name__ == "__main__":
    print(divide(10, 2))
def much_better_divide(func):
    def inner_func(a, b):
        print("We are going to divide %s by %s" % (a, b))
        return func(a, b)
    return inner_func


def better_divide(func):
    def inner_func(a, b):
        if b == 0:
            print("Oops, can't divide by zero")
            return
        else:
            return func(a, b)
    return inner_func


@much_better_divide
@better_divide
def divide(a, b):
    return a/b


if __name__ == "__main__":
    print(divide(10, 0))7
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("%s %s" % (key, value))
        print("{} {}".format(key, value))


if __name__ == "__main__":
    print_kwargs(id1="Ram", id2="Rahim")
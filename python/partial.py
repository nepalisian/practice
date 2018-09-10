from functools import partial


def add(a,b,c):
    return a+b+c


partial_add = partial(add, a=10, c=10)


if __name__ == "__main__":
    print(add(10,20,30))
    print(partial_add(b=10))
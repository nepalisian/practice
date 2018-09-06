

def fib_iterative(count):
    n1 = 0
    n2 = 1
    fibonacci = [ 0, 1 ]
    for _ in xrange(count-2):
        fibonacci.append(n1 + n2)
        tmp = n2
        n2 = n1 + n2
        n1 = tmp

    return fibonacci


def fib_recursive(count):
    fibonacci = [0, 1]
    for i in xrange(2, count):
        fibonacci.append(fib(i))
    return fibonacci


def fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fib(position-1) + fib(position-2)


def main():
    count = int(raw_input())
    print(fib_iterative(count))
    print(fib_recursive(count))


if __name__ == "__main__":
    main()
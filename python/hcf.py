
def factors(i, smaller):
    factors_a = []
    for j in xrange(1,smaller+1):
        if i%j == 0:
            factors_a.append(j)
    return factors_a


def hcf(a, b):
    smaller = min(a,b)
    factors_a = set(factors(a, smaller))
    factors_b = set(factors(b, smaller))
    print(factors_a)
    print(factors_b)
    gcd = factors_a & factors_b
    return max(gcd)


def main():
    a = int(raw_input())
    b = int(raw_input())
    gcd = hcf(a, b)
    print(gcd)


if __name__ == "__main__":
    main()
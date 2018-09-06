

def hcf(a, b):
    if a == b:
        return a
    else:
        if a > b:
            result = hcf(a-b, b)
        else:
            result = hcf(a, b-a)
        return result


def lcm(a, b):
    return a*b/hcf(a,b)

def main():
    #input
    nums = map(int, raw_input().split(","))

    #gcd
    gcd = 0
    a = nums[0]
    for i in xrange(len(nums)-1):
        b = nums[i+1]
        gcd = hcf(a, b)
        a = gcd
    print(gcd)

    #lcm
    l = nums[0]
    for i in nums[1:]:
        l = lcm(l, i)
    print(l)

if __name__ == "__main__":
    main()
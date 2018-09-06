class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary, self.imaginary*other.real + self.real*other.imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return "%s%si" % (self.real, self.imaginary)
        else:
            return "%s+%si" % (self.real, self.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __div__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass


def main():
    c1 = Complex(2, 3)
    c2 = Complex(3, 4)
    print(c1+c2)
    print(c1-c2)
    print(c1*c2)
    print(c1==c2)
    print(c1/c2)


if __name__ == "__main__":
    main()
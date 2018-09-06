class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius



def main():
    c = Circle(3)
    print(c.area())
    print(c.circumference())


if __name__ == "__main__":
    main()
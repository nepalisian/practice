class Person:
    """
    Class for representing a person
    attributes:
        name: name of the person
        age: age of the person
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Citizenship:
    def __init__(self, country):
        self.country = country

    def get_country(self):
        return self.country


class Engineer(Person, Citizenship):
    def __init__(self, name, age, country):
        Person.__init__(self, name, age)
        Citizenship.__init__(self, country)

    def get_name(self):
        return "Engineer: " + self.name


def main():
    p1 = Engineer("Ram", 20, "Nepal")
    print(p1.get_country())
    print(p1.get_name())


if __name__ == "__main__":
    main()
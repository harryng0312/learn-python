class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, fname: str, lname: str, age: int):
        Person.__init__(self, fname, age)
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return self.fname + " " + self.lname + " " + str(self.age)


p1 = Person("Thử xem", 2)
print(p1.name)
print(p1.age)

x = Student("Mike", "Olsen", 2019)
print(str(x))

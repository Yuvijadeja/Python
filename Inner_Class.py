class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    class Laptop:
        def __init__(self, brand, cpu):
            self.brand = brand
            self.cpu = cpu


s1 = Student("Yovraj", 19)
l1 = Student.Laptop("DELL", "A9")

print(s1.name, s1.roll_no)
print(l1.brand, l1.cpu)

class Student:
    school = "School Name"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # class method
    @classmethod
    def get_school(cls):
        return cls.school

    # static method
    @staticmethod
    def info():
        print("This is a Student class")


s1 = Student(65, 84, 79)
print(s1.avg())
print(s1.get_school())
s1.info()

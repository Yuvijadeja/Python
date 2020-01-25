class A:
    def __init__(self):
        print("In A")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 1 working")


class B(A):
    def __init__(self):
        super().__init__()
        print("In B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


b1 = B()
b1.feature1()
b1.feature3()

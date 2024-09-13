class Person:
    def __init__(self,name):
        self.fullName = name

    def printName(self):
        pass

class Dev(Person):
    def printName(self):
        print(f"Tên của bạn là: {self.fullName}")

Wan = Dev("Phạm Quốc Hoàng")
Wan.printName()


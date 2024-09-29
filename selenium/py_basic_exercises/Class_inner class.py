class Student:

    def __init__(self, name, roll_no):

        self.name = name
        self.roll_no = roll_no

    def show(self):
        print(self.name, self.roll_no)


    class Laptop:

        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.cpu, self.ram)

s1 = Student('sumit', 40)
c1 = Student.Laptop('i5', '8gb')

s1.show()
c1.show()



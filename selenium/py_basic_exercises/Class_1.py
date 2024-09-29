


class myinfo():
    pass

    def __init__(self):
        self.name = "Sumit"
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = myinfo()
c2 = myinfo()
c2.name = 'Niana'


c1.compare(c2)


print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)

if c1.compare(c2):
    print("They are same")

else:
    print("They are different")


class student():

    school = 'JPPS'

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    # Instance method
    def avg(self):
        return(self.s1 + self.s2 + self.s3)/3

#     Class Method
    @classmethod
    def info(cls):
        return(cls.school)



    def location():
        print('School is located in hometown')



m1 = student(34, 54, 56)
m2 = student(32, 54, 43)

print(m1.avg())
print(m2.avg())

print(m1.info())
print(student.location())

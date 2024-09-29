
class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature A is working')


class B:

    def __init__(self):
        super().__init__()
        print('In B init')


    def feature1(self):
        print('Feature B is working')

class C(B):

    def __init__(self):
        super().__init__()
        print('In C init')


    def feature3(self):
        print('Feature C is working')

    def feat(self):
        super().feature1()



c1 = C()
c1.feat()


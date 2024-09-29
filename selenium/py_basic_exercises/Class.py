class automobile():

    def __init__(self, type, techn, wheeldrive):
        self.type = type
        self.techn = techn
        self.wheeldrive = wheeldrive

    def specs(self):
        print("Specs are -> ", self.type, self.techn, self.wheeldrive)

c1 = automobile('car', 'EV', 4)
c2 = automobile('bus', 'gas', 6)

c1.specs()
c2.specs()



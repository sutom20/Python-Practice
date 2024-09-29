
class Pycharm:

    def execute(self):
        print('Compiling')
        print('Running')

class Myeditor:

    def execute(self):
        print('Spell_check')
        print('Convention_check')
        print('Compiling')
        print('Running')

class laptop:

    def code(self, ide):
        ide.execute(self)

code_1 = laptop()

code_1.code(Pycharm)

print('*********************')

code_1.code(Myeditor)




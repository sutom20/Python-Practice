# Position argument

def cars(brand, tech, wheels = 18):
    print("brand is " + brand)
    print("tech is " + tech)
    print("{}{}".format("wheels are ", wheels))

cars('tata', 'EV', 28)

print("*********KW_Args output*********")


# keyword argument
cars(brand='tata', wheels=28, tech='EV')

# Default Argument

print("*********Default Args output*********")
cars(brand='tata', tech='EV')

print("*********Default Args with override value_output*********")
cars(brand='tata', wheels=35, tech='EV')


# Variable length Argument

def addn(*b):
    print(b)
    c = 0
    for i in b:
        c = c + i
    print(c)

print("*********Vairable length Arg output*********")

addn(1, 3, 5, 6, 10)


# Keyword variable length argument
def bikes(brand, **data):
    print(brand)
    print(data)
    for i,j in data.items():
        print(i,j)

print("*********Keyword Vairable length Arg output*********")

bikes('Fz', engine_cc =350, wheels = 'alloy', acc_0_100 = 7)


# Recursion



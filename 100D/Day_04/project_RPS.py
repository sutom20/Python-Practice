import random

user_input = int(input("Please enter your selection\n"))

print('Your selection is -> ')


def input_fun(user_input):
    if user_input == 0:
        print('R')
    if user_input == 1:
        print('P')
    elif user_input == 2:
        print('S')

input_fun(user_input)

posible_selection = [0 , 1 , 2]

comp_sel = random.choice(posible_selection)

print(f'Computer(s) selection is -> \n{comp_sel}')

if user_input == 0 and comp_sel == 2:
    print("You win")
elif comp_sel > user_input:
    print("You lose")
elif comp_sel == user_input:
    print("It's a draw")
else:
    print("You typed an invalid number, You lose")



# def comp_sel_fun(comp_sel):
#     if comp_sel == 0:
#         print('R')
#     if comp_sel == 1:
#         print('P')
#     elif comp_sel == 2:
#         print('S')
#
# comp_sel_fun(comp_sel)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resoure_data = CoffeeMaker()

available_options = Menu()
coffee_options = available_options.get_items().split('/')
coffee_options.pop(-1)
# print(coffee_options)

drink_selected = Menu()

resource_check = CoffeeMaker()


is_on = True

payment = MoneyMachine()

coffee_pricing = MoneyMachine()
# print(coffee_pricing.cost("latte"))

execute_button = CoffeeMaker()

while is_on:
    user_selection = input("What would you like ")

    if user_selection == "off":
        is_on = False
        print("Turning off the machine now")

    else:
        if user_selection == "report":
            resoure_data.report()

        elif user_selection in coffee_options:
            resource_check.is_resource_sufficient(drink_selected.find_drink(user_selection))
            # payment.process_coins()
            # print(payment.money_received)
            coffee_cost = coffee_pricing.cost(user_selection)
            print(payment.make_payment(coffee_cost))
            resoure_data.report()
            payment.report()
            execute_button.make_coffee(drink_selected.find_drink(user_selection))
            resoure_data.report()
            payment.report()









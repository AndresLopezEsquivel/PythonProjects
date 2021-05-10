from data import MENU, machine
from machine_functions import print_drinks_and_prices
from machine_functions import print_report
from machine_functions import is_valid_option
from machine_functions import there_is_enough_for
from machine_functions import buy_drink

machine_continues_working = True

while machine_continues_working:

    print('Welcome. What would you like to drink?')
    print_drinks_and_prices(MENU)
    choice = input('Select an option: espresso/latte/cappuccino. ').lower()

    if is_valid_option(choice):
        if choice == "off":
            print("Coffee machine turned off.")
            machine_continues_working = False
        elif choice == "report":
            print("Here's the resources report.")
            print_report(machine)
        else:
            if there_is_enough_for(choice, MENU, machine):
                machine = buy_drink(choice, MENU, machine)

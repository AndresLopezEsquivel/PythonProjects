from prettytable import PrettyTable


def print_drinks_and_prices(menu):
    table_drinks = PrettyTable()
    table_drinks.field_names = ['Drink', 'Cost']
    for drink in menu:
        table_drinks.add_row([drink, f"$ {menu[drink]['cost']}"])
    print(table_drinks)


def print_report(coffee_machine):
    """Print current resources left and current amount of money, both in the coffee machine"""
    # print(f"Water: {coffee_machine['resources']['water']} ml")
    # print(f"Milk: {coffee_machine['resources']['milk']} ml")
    # print(f"Coffee: {coffee_machine['resources']['coffee']} ml")
    # print(f"Money: ${coffee_machine['money']}")
    table_report = PrettyTable()
    table_report.add_column('Data', ['Water', 'Milk', 'Coffee', 'Money'])
    table_report.add_column('Value', [
        f"{coffee_machine['resources']['water']} ml",
        f"{coffee_machine['resources']['milk']} ml",
        f"{coffee_machine['resources']['coffee']} ml",
        f"$ {coffee_machine['money']}"
    ])
    print(table_report)


def is_valid_option(option_selected):
    op1 = option_selected == "espresso"
    op2 = option_selected == "latte"
    op3 = option_selected == "cappuccino"
    op4 = option_selected == "report"
    op5 = option_selected == "off"

    return True if op1 or op2 or op3 or op4 or op5 else False


def there_is_enough_for(selected_drink, menu, coffee_machine):
    """Indicates if there are enough resources to prepare the selected drink"""
    there_is_water = coffee_machine['resources']['water'] >= menu[selected_drink]['ingredients']['water']
    there_is_milk = coffee_machine['resources']['milk'] >= menu[selected_drink]['ingredients']['milk']
    there_is_coffee = coffee_machine['resources']['coffee'] >= menu[selected_drink]['ingredients']['coffee']

    if selected_drink == "espresso":
        is_enough = True if there_is_water and there_is_coffee else False
    else:
        is_enough = True if there_is_water and there_is_milk and there_is_coffee else False

    if not there_is_water:
        print('There is no water.')
    if not there_is_milk and selected_drink != "espresso":
        print('There is no milk.')
    if not there_is_coffee:
        print('There is no coffee.')

    return is_enough


def make_drink(selected_drink, menu, coffee_machine):
    """Prepare the drink selected by the costumer"""
    copy_coffee_machine = coffee_machine.copy()
    copy_coffee_machine['resources']['water'] -= menu[selected_drink]['ingredients']['water']
    copy_coffee_machine['resources']['milk'] -= menu[selected_drink]['ingredients']['milk']
    copy_coffee_machine['resources']['coffee'] -= menu[selected_drink]['ingredients']['coffee']
    print(f"Your {selected_drink} is served. Enjoy it!")
    return copy_coffee_machine


def buy_drink(selected_drink, menu, coffee_machine):
    """Buy and receive the selected drink."""
    drink_price = menu[selected_drink]['cost']
    print(f'{selected_drink} costs ${drink_price}.')
    pennies = float(input('Amount of pennies: ')) * 0.01
    nickles = float(input('Amount of nickles: ')) * 0.05
    dimes = float(input('Amount of dimes: ')) * 0.1
    quarters = float(input('Amount of quarters: ')) * 0.25
    total_received = pennies + nickles + dimes + quarters
    print(f'Total received: {total_received}')
    copy_coffee_machine = coffee_machine.copy()
    current_amount_of_money = copy_coffee_machine["money"]
    new_amount_of_money = current_amount_of_money + drink_price
    copy_coffee_machine['money'] = new_amount_of_money
    if total_received == drink_price:
        return make_drink(selected_drink, menu, copy_coffee_machine)
    elif total_received >= drink_price:
        print("Here is your change: {:.2f}".format(total_received - drink_price))
        return make_drink(selected_drink, menu, copy_coffee_machine)
    else:
        print('Sorry, that\'s not enough money. Money refunded.')
        return coffee_machine

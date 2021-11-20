# Functions

# TODO: 9. Tell user the cost of the selected drink
def insert_coins(drink_cost, machine_money):
    """Calculates if the user inserted enough money"""
    formatted_drink_cost = "{:.2f}".format(drink_cost)
    print(f"The cost of the drink is ${formatted_drink_cost}.\nPlease insert coins")
    # TODO: 8. Ask user to input coins
    # TODO: 5. Process coins.
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    # TODO: 6. Check transaction successful?
    payment = float(sum([quarters, dimes, nickels, pennies]))
    change = payment - drink_cost
    if change >= 0:
        machine_money += drink_cost
        formatted_change = "{:.2f}".format(change)
        print(f"Here is ${formatted_change} in change.")
        # TODO: 7. Make coffee.
        print(f"Here is your {user_select} ☕. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded")
    return machine_money


# TODO: 4. Check resources sufficient?
def calculate_resources(starting_water, required_water, starting_coffee, required_coffee, starting_milk, required_milk, drink_cost, money):
    """Calculates if there is enough ingredients in the machine to make the selected drink"""
    remaining_water = starting_water - required_water
    remaining_coffee = starting_coffee - required_coffee
    remaining_milk = starting_milk - required_milk
    if remaining_water < 0:
        print("Sorry, there is not enough water.")
    elif remaining_coffee < 0:
        print("Sorry, there is not enough coffee.")
    elif remaining_milk < 0:
        print("Sorry, there is not enough milk.")
    else:
        starting_water = remaining_water
        starting_coffee = remaining_coffee
        starting_milk = remaining_milk
        money = insert_coins(drink_cost, money)
    return starting_water, starting_coffee, starting_milk, money


# TODO: 2. Turn off the coffee machine by entering "off" to the prompt
# TODO: 3. Return machine resources when entering "report"
def drink_requirements(user_select, water, milk, coffee, money):
    """drink_requirements returns the ingredients and cost for the selected drink"""
    if user_select == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        formatted_money = "{:.2f}".format(money)
        print(f"Money: ${formatted_money}")
    elif user_select != "espresso" and user_select != "latte" and user_select != "cappuccino":
        print("Improper input, please try again.")
    else:
        drink_water = MENU[user_select]["ingredients"]["water"]
        drink_coffee = MENU[user_select]["ingredients"]["coffee"]
        drink_milk = MENU[user_select]["ingredients"]["milk"]
        drink_cost = MENU[user_select]["cost"]
        machine_ingredients = calculate_resources(water, drink_water, machine_coffee, drink_coffee, machine_milk, drink_milk, drink_cost, money)
        # Return the current machine water, coffee, and milk amounts
        water = machine_ingredients[0]
        coffee = machine_ingredients[1]
        milk = machine_ingredients[2]
        money = machine_ingredients[3]
        # Calculate the money in the machine
        # money = insert_coins(drink_cost, money)
    return water, milk, coffee, money



# Import variables
from drink_requirements import *
# Initializations
machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]
machine_money = 0
drink_water = 0
drink_coffee = 0
drink_milk = 0
drink_cost = 0
coffee_machine_on = True


# Start Code: While the machine is on, keep prompting user
while coffee_machine_on:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    user_select = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_select == "off":
        print("Goodbye.")
        coffee_machine_on = False
    else:
        machine_status = drink_requirements(user_select, machine_water, machine_milk, machine_coffee, machine_money)
        machine_water = machine_status[0]
        machine_milk = machine_status[1]
        machine_coffee = machine_status[2]
        machine_money = machine_status[3]
        print("")

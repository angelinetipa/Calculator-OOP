# import userinterface and calculator
from user_interface import UserInterface
from simple_calculator import SimpleCalculator

ui = UserInterface()
calc = SimpleCalculator()

try_again = ""
while try_again != "no":
    # input for math operation
    operation = ui.ask_operation()

    # input for two numbers
    num1 = ui.ask_num()
    num2 = ui.ask_num()

    # if math operation is addtion, output sum of two numbers
    if operation == "1":
        calc.add(num1, num2)

    # if math operation is subtraction, output difference of two numbers
    if operation == "2":
        calc.subtract(num1, num2)

    # if math operation is multiplication, output product of two numbers
    if operation == "3":
        calc.multiply(num1, num2)

    # if math operation is division, output quotient of two numbers
    if operation == "4":
        calc.divide(num1, num2)

    # input for try again
    try_again = input("Do you want to try again (yes/no)?😁  ").strip().lower()

# last message
ui.last_message( )
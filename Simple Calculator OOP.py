# import userinterface and calculator
from user_interface import UserInterface
from simple_calculator import SimpleCalculator

ui = UserInterface()
calc = SimpleCalculator()

try_again = ""
while try_again != "no":
    # input for math operation
    operation = ui.ask_user_operation()

    # input for two numbers
    num1 = ui.ask_user_number()
    num2 = ui.ask_user_number()

    # if math operation is addtion, output sum of two numbers
    if operation == "1":
        answer = calc.add(num1, num2)
        ui.display_sum(num1, num2, answer)

    # if math operation is subtraction, output difference of two numbers
    if operation == "2":
        answer = calc.subtract(num1, num2)
        ui.display_difference(num1, num2, answer)

    # if math operation is multiplication, output product of two numbers
    if operation == "3":
        answer = calc.multiply(num1, num2)
        ui.display_product(num1, num2, answer)
    # if math operation is division, output quotient of two numbers
    if operation == "4":
        answer = calc.divide(num1, num2)
        ui.display_quotient(num1, num2, answer)
        
    # input for try again
    try_again = input("Do you want to try again (yes/no)?😁  ").strip().lower()

# last message
ui.last_message( )
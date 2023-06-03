# class Calculator
class SimpleCalculator:

    # def add
    def add(self, num1, num2):
        sum = num1 + num2
        return sum

    # def subtract
    def subtract(self, num1, num2):
        difference = num1 - num2
        return difference
    
    # def multiply
    def multiply(self, num1, num2):
        from colorama import Fore, Back, Style
        print(f"{Fore.YELLOW}{num1} x {num2} = {Style.RESET_ALL}", float(num1) * float(num2))

    # def divide
    def divide(self, num1, num2):
        from colorama import Fore, Back, Style
        print(f"{Fore.CYAN}{num1} / {num2} = {Style.RESET_ALL}", float(num1) / float(num2))

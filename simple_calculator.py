# class Calculator
class Simple_Calculator:

    # def add
    def add(self, num1, num2):
        try:
            return f"{num1} + {num2} = ", float(num1) + float(num2)
        # execute this when there is an exception
        except ValueError as e:
            print ("Error: ", e)

    # def subtract
    def subtract(self, num1, num2):
        try:  
            return f"{num1} - {num2} = ", float(num1) - float(num2)
        # execute this when there is an exception
        except ValueError as e:
            print ("Error: ", e)

    # def multiply
    def multiply(self, num1, num2):
        try:
            return f"{num1} x {num2} = ", float(num1) * float(num2)
        # execute this when there is an exception
        except ValueError as e:
            print ("Error: ", e)

    # def divide
    def divide(self, num1, num2):
        try:
            return f"{num1} / {num2} = ", float(num1) / float(num2)
        # execute this when there is an exception
        except ValueError as e:
            print ("Error: ", e)
        except ZeroDivisionError as e:
            print("Error: ", e)
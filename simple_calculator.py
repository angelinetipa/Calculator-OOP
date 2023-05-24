# class Calculator
class SimpleCalculator:

    # def add
    def add(self, num1, num2):
        return (f"{num1} + {num2} = ", float(num1) + float(num2))

    # def subtract
    def subtract(self, num1, num2):
        return f"{num1} - {num2} = ", float(num1) - float(num2)

    # def multiply
    def multiply(self, num1, num2):
        return f"{num1} x {num2} = ", float(num1) * float(num2)

    # def divide
    def divide(self, num1, num2):
        return f"{num1} / {num2} = ", float(num1) / float(num2)

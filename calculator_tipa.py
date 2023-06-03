from simple_calculator import SimpleCalculator

class CalculatorTipa(SimpleCalculator):
    def remainder_ofdiv(self, num1, num2):
        remainder = num1 % num2
        return remainder
    
    def exponent(self, num1, num2):
        exponential_power = num1 ** num2
        return exponential_power
    
    def integer_division(self, num1, num2):
        integer_quotient = num1 // num2
        return integer_quotient
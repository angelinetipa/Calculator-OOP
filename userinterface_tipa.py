from user_interface import UserInterface

class UserInterfaceTipa(UserInterface):
    def ask_user_operation(self):
        import time, os
        from colorama import Fore, Back, Style

        print(f"\n{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}")
        operation = ""
        while operation != "1" and operation != "2" and operation != "3" and operation != "4" and operation != "5" and operation != "6" and operation != "7": 
            operation = input(f""" \n{Fore.MAGENTA}{Style.BRIGHT}> > >  1. Addition {Fore.GREEN}2. Subtraction {Fore.YELLOW}3. Multiplication {Fore.CYAN}4. Division 
            {Fore.LIGHTRED_EX}5. Modulus {Fore.LIGHTMAGENTA_EX}6. Exponent  {Fore.LIGHTGREEN_EX}7. Integer Division  < < <
            \n{Style.RESET_ALL}Choose the number of math operation you would like to use:  """).strip()
            # execute this when there is an exception
            if operation != "1" and operation != "2" and operation != "3" and operation != "4" and operation != "5" and operation != "6" and operation != "7":
                print (f"{Fore.RED}Invalid Input. Choose only the number from the given math operation ‼")
            else:
                return operation
            time.sleep(2.5)
            os.system("cls")  
    
    def display_remainder(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.LIGHTRED_EX}{num1} / {num2} = {Style.RESET_ALL}", answer)

    def display_exponentialpow(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.LIGHTMAGENTA_EX}{num1} ^ {num2} = {Style.RESET_ALL}", answer)

    def display_integerquot(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.LIGHTGREEN_EX}{num1} / {num2} = {Style.RESET_ALL}", answer)
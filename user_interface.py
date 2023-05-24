# class userinterface
class UserInterface:
    
    # def ask_operation
    def ask_operation(self):
        import time, os
        from colorama import Fore, Back, Style, init

        print(f"\n{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}")
        operation = ""
        while operation != "1" and operation != "2" and operation != "3" and operation != "4": 
            operation = input(f""" \n{Fore.MAGENTA}{Style.BRIGHT}> > >  1. Addition {Fore.GREEN}2. Subtraction {Fore.YELLOW}3. Multiplication {Fore.CYAN}4. Division   < < <
            \n{Style.RESET_ALL}Choose the number of math operation you would like to use:  """).strip()
            # execute this when there is an exception
            if operation != "1" and operation != "2" and operation != "3" and operation != "4":
                print (f"{Fore.RED}Invalid Input. Choose only the number from the given math operation ‼")
            else:
                return operation
        time.sleep(0.5)
        os.system("cls")    

    # def ask_2num
    def ask_num(self):
        num1, num2 = input("Enter your two numbers(add space between them):  ").split()  
        return num1, num2
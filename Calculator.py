import os                                                               # importing os to clear the screen for second calculation

print("Hi I'm a calculater\n\n")


def calculate():                                                        # function which except values and calculate accordingly

    try:                                                                # Getting first value
        a = int(input('what is your first value\n'))
                                                                                
    except ValueError:                                                  # excepting Errors
        print("\nOops!  That was no valid number.  Try again...")
        a = float(input('\n\nwhat is your first value\n'))
    
    
    try:
        b = float(input('\nwhat is your second value\n'))               # Getting second value
    except ValueError:                                                  # excepting Errors
        print("\nOops!  That was no valid number.  Try again...")
        b = float(input('\n\nwhat is your first value\n'))

    expression = input('\nWhat is the expression\n')                    # Getting operations to calculate

    if expression == '+':                                               # Addition
        answer = str(a + b)
        print('answer = ' + answer)

    elif expression == '-':                                             # Substraction
        answer = str(a - b)
        print('answer = ' + answer)

    elif expression == '*':                                             # Multiplication
        answer = str(a * b)
        print('answer = ' + answer)

    elif expression == '**':                                            # Exponent
        try:
            answer = str(a ** b)
            print('answer = ' + answer)
        except OverflowError:
            print("\nOops!  That was a really big number. Sorry...")

    elif expression == '/':                                             # Division
        answer = str(a / b)
        print('answer = ' + answer)

    elif expression == '//':                                            # Interger Division
        answer = str(a // b)
        print('answer = ' + answer)


    next = input("\n\nWana find another one??  y/n\n")                    # Asking If the user want's to continue or exit 
    
    if next == 'y' or next == 'yes':
        cls()                                                           # Clearing the screen

    else:
        exit()                                                          # Killing the code

def cls():                                                              # clearing the screen function
    os.system("CLS")


if __name__ == '__main__':
    while True:
        calculate()                                                     # Calling function Calculate

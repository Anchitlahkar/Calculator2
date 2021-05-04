import os                                                               

print("Hi I'm a calculator\n\n")


def calculate():                                                        

    try:                                                                
        a = float(input('what is your first value\n'))
                                                                                
    except ValueError:                                                  
        print("\nOops!  That was no valid number.  Try again...")
        a = float(input('\n\nwhat is your first value\n'))
    
    
    try:
        b = float(input('\nwhat is your second value\n'))               
    except ValueError:                                                  
        print("\nOops!  That was no valid number.  Try again...")
        b = float(input('\n\nwhat is your first value\n'))

    expression = input('\nWhat is the expression\n')                    

    if expression == '+':                                               
        answer = str(a + b)
        print('answer = ' + answer)

    elif expression == '-':                                             
        answer = str(a - b)
        print('answer = ' + answer)

    elif expression == '*':                                             
        answer = str(a * b)
        print('answer = ' + answer)

    elif expression == '**':                                            
        try:
            answer = str(a ** b)
            print('answer = ' + answer)
        except OverflowError:
            print("\nOops!  That was a really big number. Sorry...")

    elif expression == '/':                                            
        answer = str(a / b)
        print('answer = ' + answer)

    elif expression == '//':                                            
        answer = str(a // b)
        print('answer = ' + answer)


    next = input("\n\nWana find another one??  y/n\n")                     
    
    if next == 'y' or next == 'yes':
        cls()                                                           

    else:
        exit()                                                          

def cls():                                                              
    os.system("CLS")


if __name__ == '__main__':
    while True:
        calculate()                                                     

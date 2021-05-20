import os

def inputValue():
    try:
        num1 = int(input("Please enter the first number\n"))
        num2 = int(input("\nPlease enter the second number\n"))

    except ValueError:
        os.system("CLS")
        print("ValueError...\n")
        inputValue()
        os.system("CLS")

    print('\nAddition    : ', num1+num2)
    print('Subtraction : ', num1-num2)
    print('Multiplication: ', num1*num2)
    print('Division    : ', num1/num2)
    print('Square of number 1 : ', num1**2)
    print('Square of number 2 : ', num2**2)


    input()
    os.system("CLS")

while True:
    inputValue()

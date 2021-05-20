# Writing a program to display the first 10 multiples of any number.

import os

while True:
    num = int(
        input("Enter a number to find the multiplication table of that number: \n"))

    print("\n")

    for i in range(0, 11):
        value = num*i
        print(num, '*', i, ' :', value)

    user_y_n = input("\n\nWant to find another one??  y/n: \t")

    y_n = user_y_n.lower()

    if 'y' in y_n:
        os.system("CLS")

    else:
        exit()

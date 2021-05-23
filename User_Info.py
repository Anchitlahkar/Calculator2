import os

user_info = {
    "Name:": '',
    "Class:": '',
    "Section:": '',
    "Roll_No:": '',
    "Address:": '',
    "Phone:": '',
}

user_Query =[]
user_full_data =[]

for i in user_info:
    user_info[i] = input('Please Enter Your '+ i+'  ')
    user_Query.append(i)
    
    value = user_info[i]
    user_full_data.append(value)

os.system("CLS")

for i in range(0, len(user_info)):
    print(user_Query[i],' ',user_full_data[i])

input("\n\nExit")

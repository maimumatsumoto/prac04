#//1. Basic list operations//#
numbers=[]
number1=int(input("Number: "))
number2=int(input("Number: "))
number3=int(input("Number: "))
number4=int(input("Number: "))
number5=int(input("Number: "))

numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/5))


#//2. Woefully inadequate security checker//#

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


username= input("Enter your username")

if username in usernames:
    print("Access granted")

if not username in usernames:
    print("Access denied")
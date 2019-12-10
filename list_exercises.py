#//1. Basic list operations//#
"""numbers=[]
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

"""


#//3. List comprehensions//#
"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: use a list comprehension to create a list of all of the full_names in lowercase format


#for i in range(len(full_names)):
#    full_names[i]=full_names[i].lower()
#print(full_names)

lowercase_full_names =[name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers from the above list of strings

numbers = [int(i) for i in almost_numbers]
print(numbers)

# TODO: use a list comprehension to create a list of only the numbers that are greater than 9 from the numbers (not strings) you just created

greater_9 = [number for number in numbers if number>9]
print(greater_9)

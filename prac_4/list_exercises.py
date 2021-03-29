
numbers = []
for i in range(5):
 number = int ( input ( "Enter  numbers :" ) )
 numbers = numbers + [number]
print (numbers)
print("Number:{}".format(numbers[0]))
print("Number:{}".format(numbers[1]))
print("Number:{}".format(numbers[2]))
print("Number:{}".format(numbers[3]))
print("Number:{}".format(numbers[4]))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The largest number is {}".format(max(numbers)))
print("The smallest number is {}".format(min(numbers)))
print("The average of the numbers is {}".format((sum(numbers)/len(numbers))))

#security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_username = input("Enter your username: ")
for j in range(len(usernames)):
 if input_username == usernames[j]:
     print("Access granted")
     break
 else:
     print("Access denied")

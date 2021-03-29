numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]  = 3
# numbers[-1] = 2
# numbers[3]  = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#1 Change the first element of numbers to "ten"
numbers[0] ='10'
print(numbers)

#2Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

#3Get all the elements from numbers except the first two
numbers_1 = numbers[2:7]
print(numbers_1)

#4Check if 9 is an element of numbers
CHECK = 9
if CHECK in numbers:
    print("{} is a element of numbers".format(CHECK))
else:
    print("{} is not a element of numbers".format(CHECK))
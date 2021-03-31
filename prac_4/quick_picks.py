import random
NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45
number_of_line = int(input( "How many quick picks ?"))
while number_of_line < 0:
    print("Enter numbers greater than 0")
    number_of_line = int ( input ( "How many quick picks ?" ) )
for i in range(number_of_line):
    quick_pick =[]
    for j in range(NUMBERS_PER_LINE):
     random_number = random.randint ( MIN,MAX )
     while random_number in quick_pick :
         random_number = random.randint ( MIN, MAX)
     quick_pick.append (random_number )
    quick_pick.sort ()
    print ( " ".join ( "{:2}".format ( number ) for number in quick_pick ) )

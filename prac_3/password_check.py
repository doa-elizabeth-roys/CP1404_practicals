MIN_LENGTH = 8
password = input("Enter password: ")
valid_input = False
while not valid_input:
 if len(password)<MIN_LENGTH:
    print("Enter a password with atleast {} characters".format(MIN_LENGTH))
    password = input ( "Enter password: " )
 else:
    for i in range(len(password)):
        print("*",end='')
    valid_input = True
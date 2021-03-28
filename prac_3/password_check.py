MIN_LENGTH = 8

def main() :
 password = get_password(MIN_LENGTH)
 print_asterisks(ACTUAL_LENGTH)

ACTUAL_LENGTH = len(password )

  if ACTUAL_LENGTH < MIN_LENGTH :
    print ( "Enter a password with atleast {} characters".format ( MIN_LENGTH ) )
    password = input ( "Enter password: " )
  else :
    print_asterisk(ACTUAL_LENGTH)

def print_asterisk(ACTUAL_LENGTH):
  for i in range (len( password )):
   print ( "*", end='' )
main ()


MENU = """C - Convert Celsius to Fahrenheit
          F - Convert Fahrenheit to Celsius
          Q - Quit"""
print(MENU)

def main():
 choice = input(">>> ").upper()

 while choice != "Q":
   if choice == "C":
       celsius = float(input("Celsius: "))
       Fahrenheit = celsius_to_fahrenheit(celsius)
       print ( "Fahrenheit is {:.2f} F".format (Fahrenheit))       # fahrenheit = celsius * 9.0 / 5 + 32
   elif choice == "F":
      fahrenheit = float(input("Fahrenheit:"))
      celsius = fahrenheit_to_celsius(fahrenheit)
      print("Celsius is {:.2f} C".format(celsius))
   else:
     print("Invalid option")
   print(MENU)
   choice = input(">>> ").upper()
 print("Thank you.")

def celsius_to_fahrenheit(c):
 return c * 9.0 / 5 + 32

def fahrenheit_to_celsius(f):
 return (5 / 9 * (f - 32))
main()


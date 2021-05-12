from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxi = None
    total_cost = 0
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input().lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_chosen = int(input("Choose taxi:"))
            try:
                taxi = taxis[taxi_chosen]
            except IndexError:
                print("Invalid entry")
            print("Bill to date:$ {}".format(current_bill))
            print(MENU)
            choice = input().lower()
        elif choice == "d":
         if taxi:
            taxi.start_fare()
            distance_to_travel = float(input("Drive how far?"))
            taxi.drive(distance_to_travel)
            current_bill = taxi.get_fare()
            print("Your {self.name} trip cost you $ {self.get_fare}".format(self=taxi))
            print("Bill to date: ${}".format(current_bill))
            total_cost += current_bill
            print(MENU)
            choice = input().lower()
         else:
          print("Please choose a taxi first")


        else:
             print("Invalid choice")
             print("Bill to date: ${:.2f}".format(total_cost))
             print(MENU)
             choice = input(">>> ").lower()
    print("Total trip cost:{}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    i = 0
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i]))
        i = +1


main()

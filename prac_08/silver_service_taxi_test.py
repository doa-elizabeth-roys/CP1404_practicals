from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    new_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(new_taxi)
#test get fare[
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(" The fare is ${:.2f}".format(taxi.get_fare()))

main()

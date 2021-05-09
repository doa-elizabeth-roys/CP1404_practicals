from prac_08.taxi import Taxi


def main():
    """Demo test code to test taxi."""

    taxi = Taxi("Prius 1", 100, 1.23)
    taxi.drive(40)
    taxi.current_fare = Taxi.get_fare
    print("{self.name} has {self.fuel} units of fuel, it drive {self.current_fare_distance}km on at"
          " ${self.price_per_km}/km.".format(self=taxi))

# Restart the meter
    taxi.start_fare()
    taxi.drive(100)
    print("{self.name} has {self.fuel} units of fuel, it drive {self.current_fare_distance}km on at"
          " ${self.price_per_km}/km.".format(self=taxi))

main()

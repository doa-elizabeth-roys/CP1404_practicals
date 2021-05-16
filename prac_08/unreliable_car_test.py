from prac_08.unreliable_car import UnreliableCar
import random

def main():
    """Demo test code to test unreliable car."""
    car = UnreliableCar("Getz", 120)
    number = random.randint(0, 100)
    car.drive(number)
    print("{self.name} has {self.fuel} unit fuel and has travelled {self.distance}km.".format(self = car))

main()
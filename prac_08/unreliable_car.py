from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = random.uniform(0, 100)

    def drive(self, number):
        """Drive the car if random number is less
         than the car's reliability.
        """
        if number < self.reliability:
            self.distance = self.fuel
        else:
            self.distance = 0
        return self.distance

    def _str_(self):
        """Return the car's name,fuel and odometer reading"""
        return ("{} has {} unit fuel and has travelled {} distance".format(self.name, self.fuel, self.distance))

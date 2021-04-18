
CURRENT_YEAR = 2021
AGE = 50

class Guitar:
    """"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string in the following format."""
        return ("{} ({}) : ${:,}".format(self.name, self.year, self.cost))

    def get_age(self):
        """Return how old the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is 50 or more years old."""
        return self.get_age() >= AGE


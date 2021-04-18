from prac_06.guitar import Guitar

CURRENT_YEAR = 2021

def main():
    """Code to test Guitar."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another guitar", 2013, 1005.56)

#Testing if get_age() method and is_vintage work
    print("{} get_age() - Expected {}. Got {}" .format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}" .format(another_guitar.name, 8, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}" .format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}" .format(another_guitar.name, False, another_guitar.is_vintage()))

main()
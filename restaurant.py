"""A class that can be used to represent a restaurant"""

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """description of the restaurant"""
        print(self.restaurant_name.title() +
              " is a great restaurant that serves " +
              self.cuisine_type.title() +
              ".")

    def open_restaurant(self):
        """Indicates restaurant is open."""
        print(self.restaurant_name.title() +
              " is now open.")


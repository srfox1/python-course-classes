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

restaurant = Restaurant("rita's", "sea food")
restaurant_2 = Restaurant("mario's pizza", "italian food")
restaurant_3 = Restaurant("Juny's", "jamaican food")

print("This restaurant is called " +
      restaurant.restaurant_name.title() +
      " and they serve " +
      restaurant.cuisine_type.title() +
      ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
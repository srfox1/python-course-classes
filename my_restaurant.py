from restaurant import Restaurant


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
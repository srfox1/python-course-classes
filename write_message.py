filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("Hello World!\n")

with open(filename, 'a') as file_object:
    file_object.write(("I love programming."))
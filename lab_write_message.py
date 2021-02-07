filename = "guest.txt"





active = True
user_name = ''

while active:
    user_name = input("What is your first name: ")

    if user_name == '':
        print("Please enter your name.")
    else:
        with open(filename, 'w') as file_object:
            file_object.write("It looks like your name is " + user_name + ".")
            active = False
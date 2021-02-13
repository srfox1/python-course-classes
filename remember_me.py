import json

#Load the username, if it has been stored previously
#Otherwise, Prompt for the username and store it.



filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")

except FileNotFoundError:
    username = input("WWhat is your name? ")

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")


class User():
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, height):
        """Initialize first name and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        """Description of the user."""
        print("Hello, my name is " +
              self.first_name.title() +
              " " +
              self.last_name.title() +
              "." +
              " I am " +
              str(self.age) +
              " year old and " +
              str(self.height) +
              " inches tall.")

    def greeting(self):
        """User Greeting to someone"""
        print("Hi, i'm " + self.first_name + ". It's nice to meet you.")

first_user = User("Jeriah", "Robinson", 3, "36")

first_user.describe_user()
first_user.greeting()


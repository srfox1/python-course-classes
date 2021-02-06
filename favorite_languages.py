from collections import OrderedDict

favorite_laguages = OrderedDict()

favorite_laguages['jen'] = "python"
favorite_laguages["sarah"] = "c"
favorite_laguages["edward"] = "ruby"
favorite_laguages["phil"] = "python"

for name, language in favorite_laguages.items():
    print(name.title() + "'s favorite language is " + language.title() + "." )


from random import randint



class Die():
    """A simple attempt to model a dice."""
    def __init__(self, color, side = 6):
        """Attributes of a die"""
        self.color = color
        self.side = side

    def roll_dice(self):
        """imulates rolling a dice."""
        side = randint(1, 6)
        return side

new_dice = Die('blue')
print(new_dice.color)
print(new_dice.side)

print("My dice color is " + new_dice.color + ".")
print("The number on the dice is " + str(new_dice.roll_dice()) + "!")
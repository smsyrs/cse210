import random

# 1) Add the class declaration. Use the following class comment.
"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
class Die:
    def __init__(self):
            self.value = 0
            self.points = 0
    def roll(self):
        self.value = random.randint(1,6)
        if self.value == 5:
            self.points = 50
        elif self.value == 1:
            self.points = 100
        else:
            self.points= 0

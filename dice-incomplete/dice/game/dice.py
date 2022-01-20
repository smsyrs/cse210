import random
class Die:
    def __init__(self):
        def self(Die):
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

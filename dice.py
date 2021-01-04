from random import randint

class Die():
    """Represent a die"""
    def __init__(self, side=6):
        """Initialize die"""
        self.side = side

    def roll_die(self):
        """Return a number between 1 and the number of sides"""
        return randint(1, self.side)

#make a 6 sided die and show results of 10 rolls
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("\n10 rolls of a 6-sided die:")
print(results)

#make a 10 sided die and show results of 10 rolls
d10 = Die(side=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)


print("\n10 rolls of a 10-sided die:")
print(results)

#make a 20 sided die and show results of 10 rolls
d20 = Die(side=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)


print("\n10 rolls of a 20-sided die:")
print(results)

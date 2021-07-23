# 9-14 骰子
from random import randint


class Die:
    """模拟骰子"""
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        """投骰子"""
        result = randint(1, self.sides)
        return result


print("Let's go!")

print("6 sides:")
die_6s = Die()
for i in range(10):
    j = str(die_6s.roll_die())
    print('\t' + j)

print("10 sides:")
die_10s = Die(10)
for i in range(10):
    j = str(die_10s.roll_die())
    print('\t' + j)

print("20 sides:")
die_20s = Die(20)
for i in range(10):
    j = str(die_20s.roll_die())
    print("\t" + j)

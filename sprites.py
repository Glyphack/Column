import random
from config import shape_colors, number_of_colors

class faller(object):  # *
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(shape_colors[:number_of_colors-1])
        self.rotation = 0
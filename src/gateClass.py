import numpy as np

class gate:
    def __init__(self):
        self.b = 0.0
        self.w1 = 0.0
        self.w2 = 0.0

    def __init__(self, b, w1, w2):
        self.b = b
        self.w1 = w1
        self.w2 = w2

    def show_weight(self):
        print(f'b = {self.b}, w1 = {self.w1}, w2 = {self.w2}')

    def op(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        b = self.b

        y = np.sum(w*x) + b

        if y <= 0:
            return 0
        else:
            return 1

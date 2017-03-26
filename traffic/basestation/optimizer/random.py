import numpy as np


class RandomOptimizer:
    def optimize(self, state=None):
        s1 = np.random.randint(0, 10)
        s2 = np.random.randint(0, 10)
        s3 = np.random.randint(0, 10)
        s4 = np.random.randint(0, 10)
        return [s1, s2, s3, s4]


class StaticRandomOptimizer:
    def __init__(self):
        self.s1 = np.random.randint(0, 50)
        self.s2 = np.random.randint(0, 50)
        self.s3 = np.random.randint(0, 50)
        self.s4 = np.random.randint(0, 50)

    def optimize(self, state=None):
        return [self.s1, self.s2, self.s3, self.s4]

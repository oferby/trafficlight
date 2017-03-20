import numpy as np


class RandomOptimizer:
    def optimize(self, state=None):
        s1 = np.random.randint(0, 10)
        s2 = np.random.randint(0, 10)
        s3 = np.random.randint(0, 10)
        s4 = np.random.randint(0, 10)
        return [s1, s2, s3, s4]

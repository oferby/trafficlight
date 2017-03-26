import random
import state
import simple


def get_optimizer(param=None):
    # return state.SimpleMaxWaitingTime(30)
    return random.StaticRandomOptimizer()

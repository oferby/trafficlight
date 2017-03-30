import random
import state
import simple


def get_optimizer(param=None):
    # return state.SimpleMaxWaitingTime(30)
    return state.SimpleMaxState(50)
    # return state.SimpleMaxRate(50)
    # return random.StaticRandomOptimizer()

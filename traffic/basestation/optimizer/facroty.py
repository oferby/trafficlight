import random
import state
import simple


def get_optimizer(param=None):
    return state.SimpleMaxState(50)

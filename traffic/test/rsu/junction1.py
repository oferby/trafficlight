import numpy as np
import time

import threading as th

from traffic.basestation.models import road
from traffic.basestation.optimizer import factory

# in params

# k,x0, mean, sdt, in_zc, in_nzc
samples = [[1, 5, 2, 1.2, 5, 10], [1, 5, 2, 1.2, 5, 5], [1, 5, 2, 1.2, 15, 5], [1, 5, 2, 1.2, 15, 5]]

# out params
green_cycle = [5, 5, 5, 5]

roads = []


def _switch_to_red():
    for r in roads:
        r.switch_to_red()


def main():
    for i in range(4):
        roads.append(road.Road(i, samples[i]))

    optimizer = factory.get_optimizer()
    while True:
        states = []
        state_list = []
        for i in range(len(roads)):
            s = roads[i].get_stats()
            state_list.append(s['num_of_cars'])
            state_list.append(s['max_wait_time'])
            state_list.append(s['in_rate'])
            states.append(s)
        lights_schedule = optimizer.optimize(states)
        print (state_list + lights_schedule)
        for i in range(len(lights_schedule)):
            roads[i].switch_to_green()
            for j in range(lights_schedule[i]):
                for r in roads:
                    r.run()
                time.sleep(0.01)
            roads[i].switch_to_red()


if __name__ == '__main__':
    main()

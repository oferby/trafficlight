import collections
import numpy as np
import time

from traffic.basestation.models import car


# k - curve steepness
# x0 - x mid point
# l curve max value


class Road:
    # k, x0, mean, sdt, in_zc, in_nzc
    def __init__(self, uuid, params):
        self.cars = collections.deque()
        self.uuid = 'lights %s' % uuid
        self.is_green = False
        self.k = params[0]
        self.x0 = params[1]
        self.s1 = np.random.normal(params[2], params[3], 1000)
        self.max_out = int(round((max(self.s1))))
        self.in_zc = params[4]
        self.in_nzc = params[5]
        self.sec = 0
        self.zero_time = np.random.randint(0, self.in_zc + self.in_nzc)
        print('Max out: %s' % self.max_out)

    def run(self):
        self.sec += 1
        self.update_cars()
        self.add_cars()
        self.remove_cars()

    def switch_to_green(self):
        print('***********  %s: light is green **************' % self.uuid)
        print('%s cars in queue' % len(self.cars))
        self.sec = 0
        self.is_green = True

    def switch_to_red(self):
        if self.is_green:
            print('***********  light is red **************')
            print('%s cars in queue' % len(self.cars))
            self.sec = 0
            self.is_green = False

    def _get_out_rate(self):
        return int(round(self.max_out / (1 + np.exp(-self.k * (self.sec - self.x0)))))

    def update_cars(self):
        for c in self.cars:
            c.update('')

    def add_cars(self):
        if self.zero_time > self.in_zc + self.in_nzc:
            self.zero_time = 0
        if self.zero_time > self.in_zc:
            self._add_cars()
        self.zero_time += 1

    def _add_cars(self):
        in_rate = int(round(self.s1[np.random.randint(0, len(self.s1))]))
        # print('%s: Adding %s cars' % (self.uuid, in_rate))
        if in_rate != 0:
            for j in range(in_rate):
                c = car.Car('mac%s' % time.time(), '')
                self.cars.append(c)

    def remove_cars(self):
        if self.is_green:
            cars_to_remove = self._get_out_rate()
            if len(self.cars) < cars_to_remove:
                cars_to_remove = len(self.cars)
            # print  ('Removing %s cars from %s' % (cars_to_remove, self.uuid))
            for i in range(cars_to_remove):
                c = self.cars.pop()
                # print('Removed car %s' % c.id)

    def get_stats(self):
        num_of_cars = len(self.cars)
        stats = {
            'uuid': self.uuid,
            'num_of_cars': num_of_cars
        }

        if num_of_cars > 0:
            stats['max_wait_time'] = self.cars[0].get_wait_time_in_sec()
        else:
            stats['max_wait_time'] = 0

        return stats

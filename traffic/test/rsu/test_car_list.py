import numpy as np
import time
import collections
import threading as th

from traffic.basestation.models import car

mean, sdt, smpl = 2, 1.2, 1000
in_zc = 7
in_nzc = 10 - in_zc
s1 = np.random.normal(mean, sdt, smpl)
max_out = int(round((max(s1))))

print('Max out: %s' % max_out)

cars = collections.deque()


def add_cars():
    for c in cars:
        c.update('')
    in_rate = int(round(s1[np.random.randint(0, smpl)]))
    print('Adding %s cars' % in_rate)
    if in_rate != 0:
        for j in range(in_rate):
            c = car.Car('mac%s' % time.time(), '')
            cars.append(c)


class put_worker(th.Thread):
    def run(self):
        while True:
            add_cars()
            time.sleep(1)


class get_worker(th.Thread):
    def run(self):
        while True:
            time.sleep(10)
            num_of_cars = len(cars)
            print('%s cars in queue' % num_of_cars)
            if num_of_cars > 0:
              for i in range(max_out):
                  try:
                    c = cars.pop()
                    print('Removed car %s' % c.id)
                  except IndexError as e:
                      break




w1 = put_worker()
w1.start()

w2 = get_worker()
w2.start()


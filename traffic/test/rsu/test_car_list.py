import numpy as np
import time
import collections
import threading as th

from traffic.basestation.models import car


cars = collections.deque()

# in params

mean, sdt, smpl = 2, 1.2, 1000
in_zc = 5
in_nzc = 5
s1 = np.random.normal(mean, sdt, smpl)

# out params

max_out = int(round((max(s1))))
print('Max out: %s' % max_out)

out_rc = 10
out_gc = 10

# curve steepness
k = 1
# x mid point
xo = 5
# curve max value
l = 5


def get_out_rate(sec):
    return int(round(l / (1 + np.exp(-k * (sec - xo)))))


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
        i = 0
        while True:
            if i > in_zc + in_nzc:
                i = 0
            if i > in_zc:
                add_cars()
            i += 1
            time.sleep(1)


class get_worker(th.Thread):
    def run(self):
        i = 0
        green = False
        while True:
            if i > (out_rc + out_gc):
                i = 0
                green = False
                print('***********  light is red **************')
            if i > out_rc:
                if not green:
                    green = True
                    print('***********  light is green **************')
                num_of_cars = len(cars)
                print('%s cars in queue' % num_of_cars)
                if num_of_cars > 0:
                  for x in range(get_out_rate(i - out_rc)):
                      try:
                        c = cars.pop()
                        print('Removed car %s' % c.id)
                      except IndexError as e:
                          break
            time.sleep(1)
            i += 1



w1 = put_worker()
w1.start()

w2 = get_worker()
w2.start()


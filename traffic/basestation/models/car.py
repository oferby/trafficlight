import collections
import time


class Car:
    last_seen = None

    def __init__(self, id, location):
        self.id = id
        self.locations = collections.deque(maxlen=5)
        self.arrival_time = time.time()
        self.arrival_time = 0

    def update(self, location, update_time=time.time()):
        self.locations.append(location)
        self.arrival_time += 1

    def get_wait_time_in_sec(self):
        return self.arrival_time

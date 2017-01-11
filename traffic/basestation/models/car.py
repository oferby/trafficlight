import collections
import time


class Car:
    last_seen = None

    def __init__(self, id, location):
        self.id = id
        self.locations = collections.deque(maxlen=5)
        self.arrival_time = time.time()
        self.update(location, self.arrival_time)

    def update(self, location, update_time=time.time()):
        self.locations.append(location)
        self.last_seen = update_time

    def get_wait_time_in_sec(self):
        return round(self.last_seen - self.arrival_time)

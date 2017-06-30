import time

class Car:
    def __init__(self, mac, position, speed, acceleration, azimute):
        self.mac = mac
        self.position = position
        self.speed = speed
        self.acceleration = acceleration
        self.azimute = azimute
        self.time_of_arrival = time.time()
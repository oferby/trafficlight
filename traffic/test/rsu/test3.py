import numpy as np

class Car:
    def __init__(self,mac,speed,place):
        self.mac = mac
        self.speed = speed
        self.place = place
cars = {}

for i in range(100):

    m = np.random.randint(10)
    s = np.random.randint(50)
    p = np.random.randint(100)

    new_tx = {
        'mac': m,
        'speed': s,
        'place': p
    }


    if new_tx['mac'] in cars.keys():
        c = cars[new_tx['mac']]
        c.speed = new_tx['speed']
        c.place = new_tx['place']
        print ('change in %s speed and place' % c.mac)
    else:
        cars[new_tx['mac']] = Car(new_tx['mac'],new_tx['speed'],new_tx['place'])
        print ('%s is a new car!' % new_tx['mac'])

        

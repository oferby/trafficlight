
class Car:
    def __init__(self, mac, speed):
        self.mac = mac
        self.speed = speed



cars = {}
cars['123'] = Car('123', 55)
cars['456'] = Car('456', 43)

print ('keys: %s' % cars.keys())


new_tx = {
    'mac': '124',
    'speed': 48
}


def got_new_tx(tx):
    if tx['mac'] in cars.keys():
        c  = cars[tx['mac']]
        c.speed = tx['speed']
    else:
        cars[tx['mac']] = Car(tx['mac'], tx['speed'])

got_new_tx(new_tx)

new_tx = {
    'mac': '123',
    'speed': 68
}

got_new_tx(new_tx)

i = 0
for c in cars.values():
    print (i, c.speed, c.mac)
    i+=1









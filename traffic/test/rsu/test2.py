import numpy as np



for i in range(100):

    m = np.random.randint(10)
    s = np.random.randint(50)

    new_tx = {
        'mac': m,
        'speed': s
    }

    print(new_tx)
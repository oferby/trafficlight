class SimpleMaxState:
    def __init__(self, max_time):
        self.max_time = float(max_time)

    def optimize(self, states):
        return_state = []
        total = 0
        for s in states:
            return_state.append(s['num_of_cars'])
            total += s['num_of_cars']
        if total == 0:
            return [1, 1, 1, 1]
        total = float(total)
        for i in range(len(return_state)):
            return_state[i] = int(float(return_state[i]) / total * self.max_time)
        return return_state

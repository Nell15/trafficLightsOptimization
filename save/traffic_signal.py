# This is a save of a lightly modified version of traffic_signal.py just in case

class TrafficSignal:
    def __init__(self, roads, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.cycle = [(False, True, False, True), (True, False, True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0


    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def cycle(roads, n):
        i = 0
        for group in roads:
            if group in roads[i]:
                pass
            i += 1
        pass

    def update(self, sim):
        cycle_length = 30
        k = (sim.t // cycle_length) % 2
        self.current_cycle_index = int(k)
        
        # Finding the intersection's most crowded road
        road_n = {}                             # creates an empty dictionnary to store the number of cars on each road
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                n = len(road.vehicles)
                road_n[road] = n
        n_max = max(road_n, key=road_n.get)     # finds the most crowded road

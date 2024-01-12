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
        self.phase_number = 6 # three phase diagram

    def set_default_config(self):
        self.cycle = [(True, True, False, False, False),(False, False, False, False, False),(False, False, True, True, False),(False, False, False, False, False),(False, False, False, False, True),(False, False, False, False, False)]
        
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.dt = 1 / 60
        self.timer = 10
        self.cars = 0

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

        # method = "ontario"
        method = "netherlands"
        # please comment or uncomment one of the previous lines to chose the desired method 
        # for the interphase calculation.

        def green_time(n:int)->float:
            """Returns the suggested green time according to an extrapolation of the times 
            suggested by the 12th book of Ontario's Traffic Manual in an urban environment.
            The time has a minimum of six seconds according to France's legislation."""
            tm = 1.86 * n + 1.6
            return max(tm, 6)
        
        def clearance_time(method:str)->float:
            """Returns the theorithical value of the clearance time for the given phase.
            Values were set from calculations based on presented formulas."""
            if method == "ontario":
                cl_tm = 4 if self.current_cycle_index == 0 else 5
            else:
                # According to my calculations, we may choose a 0 as clearance time
                # because of the intersection's configuration and phase cycle when using the Dutch method.
                cl_tm = 0
            return cl_tm

        self.timer -= self.dt

        # Counting cars on the roads
        road_n = {}                             # creates an empty dictionnary to store the number of cars on each road
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                n = len(road.vehicles)
                road_n[road] = n

        ## Fixed time algorithm v1
        # if self.current_cycle_index == 0 and self.timer <= 0:
        #     self.timer = 5
        #     self.current_cycle_index = 1
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 1 and self.timer <= 0:
        #     self.timer = 30
        #     self.current_cycle_index = 2
        # elif self.current_cycle_index == 2 and self.timer <= 0:
        #     self.timer = 5
        #     self.current_cycle_index = 3
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 3 and self.timer <= 0:
        #     self.timer = 10
        #     self.current_cycle_index = 4
        # elif self.current_cycle_index == 4 and self.timer <= 0:
        #     self.timer = 12
        #     self.current_cycle_index = 5
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 5 and self.timer <= 0:
        #     self.timer = 30
        #     self.current_cycle_index = 0
        
        ## Fixed time algorithm v2
        # if self.current_cycle_index == 0 and self.timer <= 0:
        #     self.timer = clearance_time(method)
        #     self.current_cycle_index = 1
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 1 and self.timer <= 0:
        #     self.timer = 30
        #     self.current_cycle_index = 2
        # elif self.current_cycle_index == 2 and self.timer <= 0:
        #     self.timer = clearance_time(method)
        #     self.current_cycle_index = 3
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 3 and self.timer <= 0:
        #     self.timer = 10
        #     self.current_cycle_index = 4
        # elif self.current_cycle_index == 4 and self.timer <= 0:
        #     self.timer = clearance_time(method)
        #     self.current_cycle_index = 5
        #     with open('temps.txt', 'a', newline='') as f:
        #         f.write('\n')
        # elif self.current_cycle_index == 5 and self.timer <= 0:
        #     self.timer = 30
        #     self.current_cycle_index = 0

        ## Actuated time algorithm
        if self.current_cycle_index == 0 and self.timer <= 0:
            self.timer = clearance_time(method)
            self.cars = max(road_n[self.roads[2][0]], road_n[self.roads[3][0]])
            self.current_cycle_index = 1
            with open('temps.txt', 'a', newline='') as f:
                f.write('\n')
        elif self.current_cycle_index == 1 and self.timer <= 0:
            self.timer = green_time(self.cars)
            self.current_cycle_index = 2
        elif self.current_cycle_index == 2 and self.timer <= 0:
            self.timer = clearance_time(method)
            self.cars = max([road_n[self.roads[4][i]] for i in range(4)])
            self.current_cycle_index = 3
            with open('temps.txt', 'a', newline='') as f:
                f.write('\n')
        elif self.current_cycle_index == 3 and self.timer <= 0:
            self.timer = green_time(self.cars)
            self.current_cycle_index = 4
        elif self.current_cycle_index == 4 and self.timer <= 0:
            self.timer = clearance_time(method)
            self.cars = max(road_n[self.roads[0][0]], road_n[self.roads[1][0]])
            self.current_cycle_index = 5
            with open('temps.txt', 'a', newline='') as f:
                f.write('\n')            
        elif self.current_cycle_index == 5 and self.timer <= 0:
            self.timer = green_time(self.cars)
            self.current_cycle_index = 0
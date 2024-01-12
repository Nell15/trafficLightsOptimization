import numpy as np
from trafficSimulator import *
from ways import *

with open("temps.txt",'w') as file:
    pass

sim = Simulation()

# Play with these
n = 15
a = 8
b = 15
l = 100

# Nodes
WEST_RIGHT_START = (-b-l, a)
WEST_LEFT_START = (-b-l, -a)
WEST_RIGHT_START2 = (-b-l, a - 4)
WEST_LEFT_START2 = (-b-l, -a + 4)

SOUTH_RIGHT_START = (a, b+l)
SOUTH_LEFT_START = (-a, b+l)
SOUTH_RIGHT_START2 = (a - 4, b+l)
SOUTH_LEFT_START2 = (-a + 4, b+l)

EAST_RIGHT_START = (b+l, -a)
EAST_LEFT_START = (b+l, a)
EAST_RIGHT_START2 = (b+l, -a + 4)
EAST_LEFT_START2 = (b+l, a - 4)

NORTH_RIGHT_START = (-a, -b-l)
NORTH_LEFT_START = (a, -b-l)
NORTH_RIGHT_START2 = (-a + 4, -b-l)
NORTH_LEFT_START2 = (a - 4, -b-l)

WEST_RIGHT = (-b, a)
WEST_LEFT =	(-b, -a)
WEST_RIGHT2 = (-b, a - 4)
WEST_LEFT2 =	(-b, -a + 4)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)
SOUTH_RIGHT2 = (a - 4, b)
SOUTH_LEFT2 = (-a + 4, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)
EAST_RIGHT2 = (b, -a + 4)
EAST_LEFT2 = (b, a - 4)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)
NORTH_RIGHT2 = (-a + 4, -b)
NORTH_LEFT2 = (a - 4, -b)

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT2, NORTH_LEFT2, TURN_LEFT, n)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT2, WEST_LEFT2, TURN_LEFT, n)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT2, SOUTH_LEFT2, TURN_LEFT, n)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT2, EAST_LEFT2, TURN_LEFT, n)

SOUTH_INBOUND2 = (SOUTH_RIGHT_START2, SOUTH_RIGHT2)
SOUTH_OUTBOUND2 = (SOUTH_LEFT2, SOUTH_LEFT_START2)

NORTH_INBOUND2 = (NORTH_RIGHT_START2, NORTH_RIGHT2)
NORTH_OUTBOUND2 = (NORTH_LEFT2, NORTH_LEFT_START2)

WEST_INBOUND2 = (WEST_RIGHT_START2, WEST_RIGHT2)
WEST_OUTBOUND2 = (WEST_LEFT2, WEST_LEFT_START2)

EAST_INBOUND2 = (EAST_RIGHT_START2, EAST_RIGHT2)
EAST_OUTBOUND2 = (EAST_LEFT2, EAST_LEFT_START2)

sim.create_roads([
    WEST_INBOUND,   # 0
    SOUTH_INBOUND,  # 1
    EAST_INBOUND,   # 2
    NORTH_INBOUND,  # 3

    WEST_OUTBOUND,  # 4
    SOUTH_OUTBOUND,
    EAST_OUTBOUND,
    NORTH_OUTBOUND,

    WEST_INBOUND2,  # 8
    SOUTH_INBOUND2,
    EAST_INBOUND2,
    NORTH_INBOUND2,

    WEST_OUTBOUND2, # 12
    SOUTH_OUTBOUND2,
    EAST_OUTBOUND2,
    NORTH_OUTBOUND2,

    WEST_STRAIGHT,  # 16
    SOUTH_STRAIGHT, # 17
    EAST_STRAIGHT,  # 18
    NORTH_STRAIGHT, # 19

    *WEST_RIGHT_TURN,   # 20 -> 35 (exclu)
    *SOUTH_RIGHT_TURN,  # 35 -> 50 (exclu)
    *EAST_RIGHT_TURN,   # 50 -> 65 (exclu)
    *NORTH_RIGHT_TURN,  # 65 -> 80 (exclu)

    *WEST_LEFT_TURN,    # 80 -> 95 (exclu)
    *SOUTH_LEFT_TURN,   # 95 -> 110 (exclu)
    *EAST_LEFT_TURN,    # 110 -> 125 (exclu)
    *NORTH_LEFT_TURN    # 125 -> 140 (exclu)

])

def road(a): return range(a, a+n)

### Car generation used in the powerpoint:
# sim.create_gen({
# 'vehicle_rate': 10,
# 'vehicles':[[4, {'path': [2, 18, 4]}], [15, {'path': [0, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 5]}], [13, {'path': [0, 16, 6]}], [1, {'path': [8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 15]}]]
# })
###

### Test with random car generation:
gen = random_vehicle_gen(4)
sim.create_gen({
'vehicle_rate': 10,
'vehicles':gen
})
###

sim.create_signal([[0], [2], [8], [10], [1, 3, 9, 11]]) # three phases

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
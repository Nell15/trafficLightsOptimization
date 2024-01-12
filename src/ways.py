import numpy as np
import random

# Attention, these paths are relevant to the example that I study, if you are to reuse this script for another one,
# please make sure to change the following list to match your model.

paths : list = [
    [0, *range(20, 35), 5],     # West -> south
    [0, 16, 6],                 # West -> east
    [8, *range(80, 95), 15],    # West -> north

    [3, 19, 5],                 # north -> south
    [3, *range(65, 80), 4],     # north -> west
    [11, *range(125, 140), 14],   # north -> east

    [2, 18, 4],                 # east -> west
    [2, *range(50, 65), 7],     # east -> north
    [10, *range(110, 125), 13], # east -> south

    [1, 17, 7],                 # south -> north
    [1, *range(35, 50), 6],     # south -> east
    [9, *range(95, 110), 12]    # south -> west
                ]

max_queue = 15                  # Arbitrary number you may set to your liking.

def random_vehicle_gen(n:int)->list:
    """n: number of car paths you want to generate
    returns a list structured like so : [[number of cars, {'path': path}]]"""
    return [[random.randint(1, max_queue), {'path':random.choice(paths)}] for i in range(n)]
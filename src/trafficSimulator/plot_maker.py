import matplotlib.pyplot as plt
import numpy as np

def formater():
    car_index = 0
    phases = {0:[], 2:[], 4:[]} # This is to be modified if you are not using a three phase signal like I do
    # Note: either open trafficSimalator-main or change the next line to match your file's location.
    with open('temps.txt', 'r', newline='') as f:
                lines = f.read().splitlines()
    for line in lines:
        if line == "":
            car_index = 0
        else:
            phase, wait_tm = line.rstrip('\n').split(' ')
            if float(wait_tm) != 0:
                phase = int(phase)
                if phase in [1, 3, 5]:
                    phase -= 1
                phases[phase].append([car_index, float(wait_tm)])
                car_index += 1
    # for tab in phases.values():
    #     for e in tab:
    #         print(e)
    return phases

data = formater()

print(formater())

def avg(tab):
    """Returns the average waiting time for one one phase."""
    d_times = {}
    d_nb_cars = {}
    for car in tab:
        d_times[car[0]] = d_times.get(car[0], 0) + car[1]
        d_nb_cars[car[0]] = d_nb_cars.get(car[0], 0) + 1
    d_avg = {car:round(d_times[car] / d_nb_cars[car]) for car in d_times.keys()}
    return d_avg


phases_avg = {ph:avg(data[ph]) for ph in data.keys()}

## Test
# for e in phases_avg.values():
#     print("e")
#     print(e)
# print(phases_avg)

def formater_2(d):
    indexes = []
    for ph in phases_avg.values():
        for car_i in ph.keys():
            if car_i not in indexes:
                indexes.append(car_i)
    times = {phase:[] for phase in d.keys()}
    for phase in d.keys():
        for car in indexes:
            times[phase].append(d[phase].get(car, 0))
    return indexes, times


indexes, times = formater_2(phases_avg)
# print(times)
x = np.arange(len(indexes))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0


fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in times.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel("Temps d'attente (T)")
ax.set_xlabel("Position dans la file")
ax.set_title("Temps d'attente moyen selon la position dans la file")
ax.set_xticks(x + width, indexes)
ax.legend(loc='upper left')
# m = 10
m = round(max([max(lst) for lst in times.values()]) / 10 + 1) * 10

ax.set_ylim(0, m)

plt.show()
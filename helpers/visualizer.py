#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Visualizer for smart grid
"""

import matplotlib.pyplot as plt
import csv


def plot(path):
    """
    Plots houses and batteries
    :param path: string
    :return: none
    """

    with open(path, 'r') as csvfile:
        # Read file
        result = csv.reader(csvfile)

        firstln = next(result)
        district = firstln[0]
        algorithm = firstln[1]
        total_len = firstln[2]

        points = []
        lines = []
        colours = ["#0A1F56", "#785EF0", "#DC267F", "#FE6100", "#FFB000"]

        i = -1
        j = -1
        for line in result:
            # If battery, append to list with coordinates
            if 'B' in line[0]:
                i += 1
                points.append([(int(line[1]), int(line[2]))])
            elif 'H' in line[0]:
                points[i].append((int(line[1]), int(line[2])))
                j += 1
                lines.append([])
            else:
                lines[j].append([int(line[0]), int(line[1])])

        for j, group in enumerate(points):
            for indx, point in enumerate(points[j]):
                if indx == 0:
                    plt.scatter(point[0], point[1], marker='*', s=120, color=colours[j])
                else:
                    plt.scatter(point[0], point[1], marker='^', s=25, color=colours[j])

        plt.grid(b=True, which='major', color='#666666', linestyle='-')

        # Show the minor grid lines with very faint and almost transparent grey lines
        plt.minorticks_on()

        plt.grid(True, which='minor', color='#999999', linestyle='--')
        plt.title(f"Wijk {district} met algoritme {algorithm} with total length {total_len}")

    csvfile.close()
    plt.show()

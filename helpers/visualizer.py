import matplotlib.pyplot as plt
import os
import csv
import itertools


def plot(path):

    with open(path, 'r') as csvfile:
        # Read file
        result = csv.reader(csvfile)

        firstln = next(result)
        district = firstln[0]
        algorithm = firstln[1]
        total_len = firstln[2]

        points = []
        lines = []
        # colours = ['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6']
        colours = itertools.cycle(['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6'])

        i = -1
        j = -1
        for line in result:
            if 'B' in line[0]:
                i += 1
                points.append([(int(line[1]), int(line[2]))])
            elif 'H' in line[0]:
                points[i].append((int(line[1]), int(line[2])))
                j += 1
                lines.append([])
            else:
                lines[j].append([int(line[0]), int(line[1])])

        for group in points:
            for idx, point in enumerate(group):
                if idx == 0:
                    plt.scatter(point[0], point[1], marker='s', color=next(colours))
                else:
                    plt.scatter(point[0], point[1], marker='^')

        for line in lines:
            for idx, point in enumerate(line):
                if idx + 1 == len(line):
                    break
                plt.plot(point, line[idx + 1])
    plt.show()


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__)).replace("helpers", "data\\District_1_greedy.csv")
    print(path)
    plot(path)

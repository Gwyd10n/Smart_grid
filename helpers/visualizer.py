import matplotlib.pyplot as plt
import os
import csv
import itertools


def plot(path):

    with open(path, 'r') as csvfile:
        # Read file
        result = csv.reader(csvfile)

        firstln = next(result)
        # district = firstln[0]
        # algorithm = firstln[1]
        # total_len = firstln[2]

        points = []
        lines = []
        colours = ['red', 'darkgreen', 'orange', 'purple', 'lightgreen']
        # colours = itertools.cycle(['#d7191c', '#fdae61', '#ffffbf', '#abd9e9', '#2c7bb6'])

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
                    plt.scatter(point[0], point[1], marker='s', color=colours[j])
                else:
                    plt.scatter(point[0], point[1], marker='^', color=colours[j])

        plt.grid(b=True, which='major', color='#666666', linestyle='-')

        # Show the minor grid lines with very faint and almost transparent grey lines
        plt.minorticks_on()
        plt.grid(True, which='minor', color='#999999', linestyle='--')

        # for line in lines:
        #     print(line)
        #     for idx, point in enumerate(line):
        #         if idx + 1 == len(line):
        #             break
        #         plt.plot((point[0], line[idx + 1][0]), (point[1], line[idx + 1][1]), color="r")

    plt.show()


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__)).replace("helpers", "data\\results\\District_1_hillclimber.csv")
    print(path)
    plot(path)

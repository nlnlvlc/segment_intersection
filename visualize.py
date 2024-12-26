import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections as mc

def visualize(segments, intersections):

    lc = mc.LineCollection(segments)
    fig, ax = pl.subplots(figsize=(10, 10))
    ax.add_collection(lc)

    end_x = []
    end_y = []

    for seg in segments:
        end_x.append(seg[0][0])
        end_y.append(seg[0][1])
        end_x.append(seg[1][0])
        end_y.append(seg[1][1])
    plt.scatter(end_x, end_y, marker='o', edgecolors = 'blue', c="green")


    x = [x[0] for x in intersections]
    y = [x[1] for x in intersections]

    plt.scatter(x, y, marker='o', edgecolors = 'blue', c="red")

    ax.legend(labels=('Line Segments',
                      'Endpoints',
                      'Intersections'))

    plt.savefig("Intersection Plot.png")
    plt.show()

def get_inter():
    intersections = []
    inputFile = open('output.txt', "r+")
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        line.strip("\n")

    n = int(lines[0])

    for num in range(1, n + 1):
        line = lines[num]
        points = line.split(" ")
        vals = [eval(x) for x in points]

        intersections.append(vals)

    return intersections
def main():
    segments = get_data(input("Type filename: "))

    intersectections = get_inter()

    visualize(segments, intersectections)

if __name__ == '__main__':
    main()
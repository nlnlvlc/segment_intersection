# -*- coding: utf-8 -*-
"""
Nilan Lovelace (njl8879) - Programming Assignment 2: Line Segmentation

A line sweep algorithm which identifies where two segments intersect, if there is a point of intersection.
"""
import shapely
from shapely.geometry import LineString, Point

def intersects(segment1, segment2):
    '''
    Finds an intersection between two segments
    :param segment1: two endpoints (x, y) representing a line segment
    :param segment2: two endpoints (x, y) representing a line segment
    :return: if an intersecting point is found, returns the x, y pair. otherwise, returns False
    '''

    line1 = LineString([segment1[0], segment1[1]])
    line2 = LineString([segment2[0], segment2[1]])

    int_pt = line1.intersection(line2)
    if int_pt:
        point_of_intersection = int_pt.x, int_pt.y

        return point_of_intersection
    else:
        return False

def line_sweep(segments):
    '''
    performs line sweep on set of segments
    :param segments: set of line segments to be processed
    :return: a list of availabel intersections
    '''

    #empty events queue
    eq = []
    #add all 2n points in segments
    for segment in segments:
        #appropriately label points as start or end of line segment
        #start = farthest left points, end = farthest right point
        eq.append((segment[0], "start", segment))
        eq.append((segment[1], "end", segment))

    #points get sorted by x value, the y value
    #sorted from left to right then top to bottom
    eq.sort(key=lambda x: (x[0], x[1]))

    #will store active segments
    active_segments = set()

    #will store any interactions, if any
    intersections = []

    #continue this process until all events are processed
    while eq:
        #take leftmost point
        event = eq.pop(0)
        point, event_type, segment = event
        #if point is the start of a segment, check if there are active segments
        #if active segments, check if segments are intersecting
        if event_type == 'start':
          for active_segment in active_segments:
            int_pt = intersects(segment, active_segment)
            if int_pt:
              intersections.append((int_pt, active_segment, segment))
          active_segments.add(segment)
        #if end segment, remove from active segments
        elif event_type == 'end':
          active_segments.remove(segment)

    if intersections:
        intersections = [(x[0][0], x[0][1]) for x in intersections]

    return intersections

def get_data(inputFile):
    '''
    Reads formatted input file and parses into usable data
    :param inputFile: formatted input file name
    :return: set of segments
    '''
    segments = []
    inputFile = open(inputFile, "r+")
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        line.strip("\n")

    n = int(lines[0])

    for num in range(1, n + 1):
        line = lines[num]
        points = line.split(" ")
        vals = [eval(x) for x in points]
        endPoints = [(vals[0], vals[1]), (vals[2], vals[3])]
        endPoints.sort()

        segments.append((endPoints[0], endPoints[1]))

    return segments
def main():
    # read n and points from file
    segments = get_data(input("Type filename: "))

    #find intersections, if any
    intersections = line_sweep(segments)

    intSize = len(intersections)

    outputFile = open("output.txt", "w")

    print(intSize)
    toWrite = [f"{intSize}\n"]

    #only run if some intersection was found
    if intSize > 0:
        for point in intersections:
            int_pt = f"{point[0]} {point[1]}"
            print(int_pt)
            toWrite.append(int_pt + "\n")
    outputFile.writelines(toWrite)
    outputFile.close()


if __name__ == '__main__':
    main()
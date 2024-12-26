# Programming Assignment Two: Leg Segmentation
This project finds the points of intersection between a set of line segments. This project contains two programs:

1. A line sweep algorithm which identifies where two segments intersect, if there is a point of intersection.

2. A program used to visualize the line segments, their endpoints, and any points of intersection found by the line 
sweep program

## Language & Libraries

Both programs were built using Python3. The Line Sweep Program makes use of the Shapely library in order to calculate
the intersecting point of segments. If needed, it can be installed by using the following: 

```commandline
pip install shapely
```

This Visualize Program makes use of several Matplotlib and pylab features.

## Before Running

Both programs should be stored in the same directory. All output files will save to the directory of the programs. The
input file does not need to be saved to the same directory, though doing so is recommended.

## Run the Line Sweep Program

The program can be run via the commandline:
```commandline 
python3 sweep.py
```

When prompted, the program accepts a txt filename as a single input. The first line contains n, the number of points in 
the  set, followed by n number of lines representing the x and y value of two endpoints of a line segment, with
each number separated by a space 
```
x1 y1 x2 y2
```

Once the program has finished execution, it will produce a txt file following the same format as the input file, 
displaying n, the number of intersections between line segments, on the first line, followed by n number of points,
representing the x and y value of each intersecting point.

## Run the Visualization Program

**THIS PROGRAM CAN ONLY BE RAN AFTER THE LINE SWEEP PROGRAM HAS PRODUCED AN OUTPUT FILE**

The program can be run via the commandline:
```commandline
python3 visualize.py
```

The program makes use of the file of datapoints ran through the Line Sweep Program and the corresponding
output file. When prompted, type in the same filename containing the line segments used run the line sweep program. The 
program will automatically read the Line Sweep output file stored in the directory.

Once the program has finished execution, it will save a figure named "Intersection Plot.png" as well as display the
plot in the interface. Once the display interfaced is close, the program will terminate.


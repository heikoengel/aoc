#!/usr/bin/python

class LineMap(object):

    def __init__(self, incl_diag=False):
        self.incl_diag = incl_diag
        self.data = [[0 for y in range(1000)] for x in range(1000)]

    def addLine(self, start_x, start_y, end_x, end_y):
        if start_x != end_x and start_y == end_y:  # horizontal line
            if start_x > end_x:
                xdir = -1
            else:
                xdir = 1
            x = start_x
            while True:
                self.data[x][start_y] += 1
                if x == end_x:
                    break
                x += xdir
        elif start_x == end_x and start_y != end_y:  # vertical line
            if start_y > end_y:
                ydir = -1
            else:
                ydir = 1
            y = start_y
            while True:
                self.data[start_x][y] += 1
                if y == end_y:
                    break
                y += ydir
        elif start_x == end_x and start_y == end_y:  # point
            self.data[start_x][start_y] += 1
        elif self.incl_diag is True:  # diagonal line
            if start_x > end_x:
                xdir = -1
            else:
                xdir = 1
            if start_y > end_y:
                ydir = -1
            else:
                ydir = 1
            x = start_x
            y = start_y
            while True:
                self.data[x][y] += 1
                if x == end_x:
                    break
                x += xdir
                y += ydir


with open("data.log") as f:
    linemap1 = LineMap()
    linemap2 = LineMap(incl_diag=True)
    for line in f.readlines():
        if line.endswith("\n"):
            line = line[:-1]  # strip newline
        start, end = line.split(" -> ")
        start_x, start_y = [int(k) for k in start.split(",")]
        end_x, end_y = [int(k) for k in end.split(",")]
        linemap1.addLine(start_x, start_y, end_x, end_y)
        linemap2.addLine(start_x, start_y, end_x, end_y)

# Part 1
overlap_coords = 0
for x in range(len(linemap1.data)):
    for y in range(len(linemap1.data[x])):
        if linemap1.data[x][y] >= 2:
            overlap_coords += 1

print("Part 1:", overlap_coords)

# Part 2
overlap_coords = 0
for x in range(len(linemap2.data)):
    for y in range(len(linemap2.data[x])):
        if linemap2.data[x][y] >= 2:
            overlap_coords += 1

print("Part 2:", overlap_coords)

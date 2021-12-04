#!/usr/bin/python

class Board(object):
    def __init__(self):
        self.data = [[]*5]*5
        self.drawn = [[]*5]*5
        self.exclude = False

    def set_row(self, row, values):
        self.data[row] = values
        self.drawn[row] = [0]*5

    def draw(self, number):
        for row in range(5):
            for col in range(5):
                if self.data[row][col] == number:
                    self.drawn[row][col] = 1

    def check(self):
        if self.exclude:
            return False
        for row in range(5):
            if sum(self.drawn[row]) == 5:
                return True
        for col in range(5):
            if sum([r[col] for r in self.drawn]) == 5:
                return True
        return False

    def sum_unmarked(self):
        _sum = 0
        for row in range(5):
            for col in range(5):
                if self.drawn[row][col] == 0:
                    _sum += self.data[row][col]
        return _sum


draws = []
boards = {}

with open("data.log") as f:
    # read first line with draw numbers
    draws = [int(d) for d in f.readline()[:-1].split(",")]

    # read all boards
    i = 0
    while f.readline():  # skip empty separator line
        boards[i] = Board()
        for row in range(5):
            line = f.readline()
            if line.endswith("\n"):
                line = line[:-1]
            values = [int(d) for d in line.split()]
            boards[i].set_row(row, values)
        i += 1


first = None
last = None
for number in draws:
    for i in boards:
        boards[i].draw(number)
        if boards[i].check():
            boards[i].exclude = True
            result = boards[i].sum_unmarked() * number
            if first is None:
                first = result
            last = result

print("Part 1:", first)
print("Part 2:", last)

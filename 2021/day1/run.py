#!/usr/bin/python

with open("data.log") as f:
    data = f.readlines()

data = [int(d[:-1]) for d in data]

# Part One
prev = None
incr = 0
for d in data:
    if prev is not None and d > prev:
        incr += 1
    prev = d

print("Part 1:", incr)


# Part Two
incr = 0
prev = None
for i in range(3, len(data)+1):
    s = sum(data[i-3:i])
    if prev is not None and s > prev:
        incr += 1
    prev = s

print("Part 2:", incr)

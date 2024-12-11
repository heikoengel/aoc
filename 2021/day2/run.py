#!/usr/bin/python

with open("data.log") as f:
    text = f.readlines()

# Part 1
forward = 0
depth = 0
i = 0
for line in text:
    if line.endswith("\n"):
        line = line[:-1]
        instr, val = line.split(" ")
        val = int(val)
    if instr == 'forward':
        forward += val
    elif instr == 'up':
        depth -= val
    elif instr == 'down':
        depth += val
    else:
        raise ValueError()
    i += 1

print("Part 1:", forward * depth)


# Part 2
forward = 0
depth = 0
aim = 0
i = 0
for line in text:
    if line.endswith("\n"):
        line = line[:-1]
        instr, val = line.split(" ")
        val = int(val)
    if instr == 'forward':
        forward += val
        depth += aim * val
    elif instr == 'up':
        aim -= val
    elif instr == 'down':
        aim += val
    else:
        raise ValueError()
    i += 1

print("Part 2:", forward * depth)

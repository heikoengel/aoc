import sys
from data import INPUTS
from numpy import median


def fuel(val1, val2):
    val = 0
    for i in range(abs(val1 - val2)):
        val += (i+1)
    return val


# Part 1
median_val = int(median(INPUTS))
print("Part 1:", sum([abs(k - median_val) for k in INPUTS]))

# Part 2
min_cost = None
for pos in range(min(INPUTS), max(INPUTS)):
    if min_cost is not None:
        sys.stdout.write("%d: %d\r" % (pos, min_cost))
    cost = 0
    for i in INPUTS:
        cost += fuel(i, pos)
    if min_cost is not None and cost > min_cost:
        print("Part 2:", min_cost)
        break
    min_cost = cost

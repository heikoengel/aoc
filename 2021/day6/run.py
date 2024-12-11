from data import INPUTS

ages = {}
for age in range(9):
    ages[age] = 0
for age in INPUTS:
    ages[age] += 1

for day in range(256):
    if day == 80:
        print("Part 1", sum(ages.values()))
    new_ages = {}
    for age in range(0, 8):
        new_ages[age] = ages[age+1]  # decrement age
    new_ages[6] += ages[0]  # add all parents to 6
    new_ages[8] = ages[0]  # create children
    ages = new_ages

print("Part 2", sum(ages.values()))

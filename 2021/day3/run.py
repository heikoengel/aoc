#!/usr/bin/python

with open("data.log") as f:
    data = f.readlines()

data = [d[:12] for d in data]
entries = len(data)

# Part 1
epsilon = 0
gamma = 0
for bit in range(12):
    ones = len([d[bit] for d in data if d[bit] == '1'])
    if ones > entries/2:
        gamma |= (1 << (11 - bit))
    else:
        epsilon |= (1 << (11 - bit))

print("Part 1:", gamma * epsilon)


# Part 2
oxy = 0
oxy_data = data
coo_data = data

for bit in range(12):
    ones = len([d[bit] for d in oxy_data if d[bit] == '1'])
    zeros = len([d[bit] for d in oxy_data if d[bit] == '0'])
    if len(oxy_data) > 1:
        if ones >= zeros:
            oxy_data = [d for d in oxy_data if d[bit] == '1']
        else:
            oxy_data = [d for d in oxy_data if d[bit] == '0']

    ones = len([d[bit] for d in coo_data if d[bit] == '1'])
    zeros = len([d[bit] for d in coo_data if d[bit] == '0'])
    if len(coo_data) > 1:
        if zeros <= ones:
            coo_data = [d for d in coo_data if d[bit] == '0']
        else:
            coo_data = [d for d in coo_data if d[bit] == '1']

print("Part 2:", int(oxy_data[0], 2) * int(coo_data[0], 2))

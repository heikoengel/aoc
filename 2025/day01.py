with open("data01", encoding="uft-8") as f:
    data = f.readlines()

cur = 50
zeros_pt1 = 0
zeros_pt2 = 0

for line in data:
    if line.endswith("\n"):
        line = line[:-1]
    instr = line[0]
    amount = int(line[1:])

    while amount > 0:
        if instr ==  "L":
            cur = (cur - 1) % 100
        else:
            cur = (cur + 1) % 100
        if cur == 0:
            zeros_pt2 += 1
        amount -= 1
    if cur == 0:
        zeros_pt1 += 1

print(zeros_pt1)
print(zeros_pt2)

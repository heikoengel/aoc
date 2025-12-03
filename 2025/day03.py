def find_max(bank):
    maxj = 0
    maxidx = 0
    for idx, val in enumerate(bank):
        if val > maxj:
            maxj = val
            maxidx = idx
    return (maxj, maxidx)


def get_max_joltage(bankstr, num_bats):
    bank = [int(joltage) for joltage in bankstr]
    ret = ""
    start = 0
    for bat in range(num_bats):
        end = len(bank) - num_bats + bat
        maxj, maxidx = find_max(bank[start:end+1])
        ret += str(maxj)
        start += maxidx + 1
    assert len(ret) == num_bats
    return int(ret)


if __name__ == "__main__":
    with open("data03", encoding="utf-8") as f:
        data = f.readlines()

    # Pt1
    totalj = 0
    for line in data:
        totalj += get_max_joltage(line.strip(), num_bats=2)
    print(totalj)

    # Pt2
    totalj = 0
    for line in data:
        totalj += get_max_joltage(line.strip(), num_bats=12)
    print(totalj)

from textwrap import wrap


def is_valid_pt1(num):
    numstr = str(num)
    strlen = len(numstr)
    if strlen % 2 != 0:
        return True  # odd number of digits cannot be invalid
    if numstr[:(strlen>>1)] == numstr[(strlen>>1):]:
        return False
    return True


def is_valid_pt2(num):
    numstr = str(num)
    strlen = len(numstr)
    dividers = range(1, (strlen>>1) + 1)
    for div in dividers:
        elems = wrap(numstr, div)
        if len(set(elems)) == 1:
            return False
    return True


if __name__ == "__main__":
    with open("data02", encoding="utf-8") as f:
        data = f.readline().strip()
    seqs = data.split(",")

    sum_invalid = 0
    for seq in seqs:
        start, end = seq.split("-")
        for i in range(int(start), int(end)+1):
            if is_valid_pt1(i) is False:
                sum_invalid += i

    print("Part 1:", sum_invalid)

    sum_invalid = 0
    for seq in seqs:
        start, end = seq.split("-")
        for i in range(int(start), int(end)+1):
            if is_valid_pt2(i) is False:
                sum_invalid += i

    print("Part 2:", sum_invalid)

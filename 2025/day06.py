from math import prod

def get_result(op, operands):
    if op == "+":
        return sum(operands)
    return prod(operands)  # else "*"


if __name__ == "__main__":

    with open("data06", encoding="utf-8") as f:
        data = [line.strip() for line in f.readlines()]

    # Pt1
    grand_total = 0
    data_p1 = [row.split() for row in data]
    for col in range(len(data_p1[0])):
        op = data_p1[-1][col]
        ret = get_result(op, [int(row[col]) for row in data_p1[:-1]])
        grand_total += ret

    print(grand_total)

    # Pt2
    grand_total = 0
    op = None
    operands = []
    for x in range(len(data[0])):
        numstr = "".join([line[x:x+1] for line in data[:-1]])
        if data[-1][x:x+1] in ["+", "*"]:
            # new op -> list of operands for prev. op is complete, calculate
            if op is not None:
                ret = get_result(op, operands)
                grand_total += ret
            # get new op, reset list of operands
            op = data[-1][x:x+1]
            operands = []
        if numstr != " "*len(numstr):
            operands.append(int("".join(numstr)))

    ret = get_result(op, operands)
    grand_total += ret

    print(grand_total)

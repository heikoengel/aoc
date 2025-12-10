def get_area(pt0, pt1):
    return (abs(pt0[0] - pt1[0]) + 1) * (abs(pt0[1] - pt1[1]) + 1)

if __name__ == "__main__":

    with open("data09", encoding="utf-8") as f:
        # get coordinates as list of tuples
        data = [tuple(int(x) for x in line.strip().split(",")) for line in f.readlines()]

    max_area = 0
    for i, p1 in enumerate(data):
        for p2 in data[i+1:]:
            area = get_area(p1, p2)
            max_area = max(max_area, area)

    print(max_area)

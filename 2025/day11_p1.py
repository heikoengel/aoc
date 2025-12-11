if __name__ == "__main__":

    data = {}
    with open("data11", encoding="utf-8") as f:
        for line in f.readlines():
            node, *outputs = line.strip().split()
            data[node[:-1]] = outputs

    # Pt1
    start = "you"
    end = "out"
    steps = 1
    next_hops = data[start]
    paths = 0
    while steps < len(data):
        paths += sum(node == end for node in next_hops)
        hops = next_hops
        next_hops = []
        for hop in hops:
            if hop in [end, "out"]:
                continue
            next_hops.extend(node for node in data[hop])
        steps += 1

    print(paths)

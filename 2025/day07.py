if __name__ == "__main__":

    with open("data07", encoding="utf-8") as f:
        data = [list(line.strip()) for line in f.readlines()]

    # Pt 1: count splits
    splits = 0

    # Pt 2: count timelines
    rows = len(data)
    cols = len(data[0])
    timelines = [[0 for j in range(cols)] for i in range(rows)]
    timelines[0][data[0].index("S")] = 1

    for row in range(1, len(data)):
        for (idx, val) in enumerate(data[row]):
            if data[row-1][idx] in ["S", "|"]:
                if val in [".", "|"]:  # free spot or reached already via different timeline
                    data[row][idx] = "|"
                    timelines[row][idx] += timelines[row-1][idx]
                elif val == "^":  # splitter
                    data[row][idx-1] = "|"
                    timelines[row][idx-1] += timelines[row-1][idx]
                    data[row][idx+1] = "|"
                    timelines[row][idx+1] += timelines[row-1][idx]
                    splits += 1

    print(splits)

    print(sum(timelines[-1]))

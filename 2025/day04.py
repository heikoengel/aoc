def get_nadj(x, y, rmap):
    nadj = 0
    for ix in range(max(0, x-1), min(len(rmap[0])-1, x+1)+1):
        for iy in range(max(0, y-1), min(len(rmap)-1, y+1)+1):
            if iy == y and ix ==x:
                continue  # exclude checked pos
            if data[iy][ix] == "@":
                nadj += 1
    return nadj


if __name__ == "__main__":

    with open("data04", encoding="utf-8") as f:
        data = [line.strip() for line in f.readlines()]

    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    total_removed = 0
    iteration = 0

    while True:
        accessible = 0
        removable = []
        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                if data[y][x] == "@" and get_nadj(x, y, data) < 4:
                    accessible += 1
                    removable.append((x, y))

        for (x, y) in removable:
            data[y] = data[y][:x] + "." + data[y][x+1:]  # remove roll: replace @ with .
        total_removed += accessible

        if iteration == 0 or accessible == 0:
            # Pt1 result: iteration=0
            # Pt2 result: accessible=0
            print("Iteration: %d, rolls accessible: %d, total rolls removed: %d" % (
                iteration, accessible, total_removed))
        if accessible == 0:
            break
        iteration += 1

if __name__ == "__main__":

    with open("data05", encoding="utf-8") as f:
        data = [line.strip() for line in f.readlines()]

    fresh_ranges = [[int(x) for x in line.split("-")] for line in data if "-" in line]
    avail_ids = [int(line) for line in data if len(line) > 0 and "-" not in line]

    # Pt1
    fresh = 0
    for iid in avail_ids:
        for fr in fresh_ranges:
            if iid in range(fr[0], fr[1]+1):
                fresh += 1  # ingredient ID in range -> fresh
                break

    print(fresh)

    # Pt 2
    while True:
        merged_ranges = []
        for fr in fresh_ranges:
            merged = False
            for mr in merged_ranges:
                if fr[0] >= mr[0] and fr[1] <= mr[1]:
                    # fr falls fully into existing range -> discard
                    merged = True
                    break
                if fr[0] < mr[0] and (mr[0] - 1 <= fr[1] <= mr[1]):
                    # fr extends mr to the left
                    mr[0] = fr[0]
                    merged = True
                    break
                if (mr[0] <= fr[0] <= mr[1] + 1) and fr[1] > mr[1]:
                    # fr extends mr to the right
                    mr[1] = fr[1]
                    merged = True
                    break
                if fr[0] < mr[0] and fr[1] > mr[1]:
                    # fr extends mr in both directions
                    mr[0] = fr[0]
                    mr[1] = fr[1]
                    merged = True
                    break

            if merged is False:
                # no merge with any existing range in merged_ranges -> add as new
                merged_ranges.append(fr)

        if len(merged_ranges) == len(fresh_ranges):
            break  # no more changes -> done, break while loop

        fresh_ranges = merged_ranges[:]

    total_fresh = sum((r[1] - r[0]) + 1 for r in fresh_ranges)
    print(total_fresh)

from math import prod

def distance(coord_a, coord_b):
    dist_square = (coord_a[0] - coord_b[0])**2 + \
        (coord_a[1] - coord_b[1])**2 + \
        (coord_a[2] - coord_b[2])**2
    # no need to calculate sqrt, sqrt is monotonic
    return dist_square

if __name__ == "__main__":

    with open("data08", encoding="utf-8") as f:
        # get coordinates as list of tuples
        data = [tuple(int(x) for x in line.strip().split(",")) for line in f.readlines()]

    distmap = {}
    for idx, coord in enumerate(data):
        for other in data[idx+1:]:
            dist = distance(coord, other)
            if dist in distmap:
                raise ValueError("more than one pair for the same dist")
            distmap[dist] = [coord, other]

    circuits = []
    for i, dist in enumerate(sorted(distmap)):
        pair = distmap[dist]

        # check if both pairs are already somewhere in the same circuit
        skip = False
        for idx, circuit in enumerate(circuits):
            if pair[0] in circuit and pair[1] in circuit:
                skip = True
                break

        if skip is False:
            existing_circuits = []
            for idx, circuit in enumerate(circuits):
                if pair[0] in circuit:
                    existing_circuits.append(idx)
                if pair[1] in circuit:
                    existing_circuits.append(idx)

            if len(existing_circuits) > 0:
                # one junction is already in at least one existing ciruit: merge them
                for ec_idx in existing_circuits[1:]:
                    # merge existing circuits into the first and clear all others
                    circuits[existing_circuits[0]] |= set(circuits[ec_idx])
                    circuits[ec_idx] = set()
                # add the current pair to the first/merged circuit
                circuits[existing_circuits[0]] |= set(pair)

                # Pt 2: all junctions are in the same circuit
                if len(circuits[existing_circuits[0]]) == len(data):
                    print(pair[0][0] * pair[1][0])
                    break
            else:
                # none of the junctions is in an existing circuit -> add as new circuit
                circuits.append(set(pair))

        # Pt 1: 1000 junctions added in total
        if i == 1000:
            largest_circuits = []
            for c in sorted(circuits, key=lambda k: len(k), reverse=True)[:3]:
                largest_circuits.append(len(c))
            print(prod(largest_circuits))

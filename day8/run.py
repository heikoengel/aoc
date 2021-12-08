#!/usr/bin/python

digits1478 = 0
total = 0

with open("data.log") as f:
    for line in f.readlines():
        if line.endswith("\n"):
            line = line[:-1]
        pattern_str, output_str = line.split(" | ")
        patterns = pattern_str.split()
        outputs = output_str.split()

        # Part 1
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:  # 1, 7, 4, 8
                digits1478 += 1

        # Part 2
        one = set([[c for c in p] for p in patterns if len(p) == 2][0])
        seven = set([[c for c in p] for p in patterns if len(p) == 3][0])
        four = set([[c for c in p] for p in patterns if len(p) == 4][0])
        eight = set([[c for c in p] for p in patterns if len(p) == 7][0])
        a = seven - one
        nines = [set([c for c in p]) for p in patterns if len(p) == 6]
        nine = [n for n in nines if one.issubset(n) and
                four.issubset(n) and seven.issubset(n)][0]
        e = eight - nine
        twos = [set([c for c in p]) for p in patterns if len(p) == 5]
        two = [t for t in twos if e.issubset(t)][0]
        g = two - seven - four - e
        threes = [set([c for c in p]) for p in patterns if len(p) == 5]
        three = [t for t in threes if one.issubset(t)][0]
        d = three - seven - g
        b = four - seven - d
        c = two & one
        f = seven - two

        # build a map of the set required for each number with the
        # derived wiring:
        mixmap = {
            0: a | b | c | e | f | g,
            1: c | f,
            2: a | c | d | e | g,
            3: a | c | d | f | g,
            4: b | c | d | f,
            5: a | b | d | f | g,
            6: a | b | d | e | f | g,
            7: a | c | f,
            8: a | b | c | d | e | f | g,
            9: a | b | c | d | f | g,
        }

        number = 0
        for output in outputs:
            out = set([c for c in output])
            number *= 10
            number += [m for m in mixmap if mixmap[m] == out][0]
        total += number


print("Part 1:", digits1478)
print("Part 2:", total)

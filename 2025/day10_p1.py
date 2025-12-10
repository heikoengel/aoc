from itertools import combinations

def apply_seq(sequence, nlights):
    lights = [False]*nlights  # all off
    for op in sequence:
        for light in op:
            lights[light] = not lights[light]
    return lights


total_presses = 0
for lights, *buttons, joltages in map(str.split, open("data10", encoding="utf-8")):
    lights = [c=="#" for c in lights[1:-1]]
    buttons = [[int(l) for l in b[1:-1].split(',')] for b in buttons]

    btn_presses = None
    for n in range(len(buttons)):
        for seq in combinations(buttons, n):
            if lights == apply_seq(seq, len(lights)):
                btn_presses = n
                break
        if btn_presses is not None:
            break
    total_presses += btn_presses

print(total_presses)

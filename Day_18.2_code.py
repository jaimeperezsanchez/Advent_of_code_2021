from typing import Any
from math import ceil

def read_input():
    with open('./Day_18_input.txt', 'r') as f:
        data_str = f.readlines()
    data_strip = [x.strip() for x in data_str]
    return [[int(x) if x.isdigit() else x for x in line] for line in data_strip]

def add_fish_num(snf_nr_1, snf_nr_2):
    return ["["] + snf_nr_1 + [","] + snf_nr_2 + ["]"]
    
def perform_actions(snf_nr):
    changed = True
    while changed:
        changed = False
        depth = 0
        for i, c in enumerate(snf_nr):
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            if depth > 4:
                snf_nr = explode_fish_num(snf_nr, i)
                changed = True
                break
        for i, c in enumerate(snf_nr):
            if changed:
                break
            if isinstance(c, int) and int(c) > 9:
                snf_nr = split_fish_num(snf_nr, i)
                changed = True
                break
    return snf_nr

def explode_fish_num(snf_nr, i):
    left_int = snf_nr[i+1]
    right_int = snf_nr[i+3]
    for j in range(i, -1, -1):
        if isinstance(snf_nr[j], int):
            snf_nr[j] += left_int
            break
    for j in range(i + 4, len(snf_nr)):
        if isinstance(snf_nr[j], int):
            snf_nr[j] += right_int
            break
    snf_nr[i:i+5] = [0]
    return snf_nr     

def split_fish_num(snf_nr, i):
    snf_nr[i:i + 1] = ["["] + [snf_nr[i] // 2] + [","] + [ceil(snf_nr[i] / 2)] + ["]"]
    return snf_nr

def magnitude(snf_nr):
    while len(snf_nr) != 1:
        for i, c in enumerate(snf_nr):
            if isinstance(c, int) and isinstance(snf_nr[i + 2], int):
                snf_nr[i - 1:i + 4] = [3 * c + 2 * snf_nr[i+2]]
                break
    return snf_nr[0]

def main():
    data = read_input()
    max_mag = 0
    for nr_1 in data:
        for nr_2 in data:
            start_nr = add_fish_num(nr_1, nr_2)
            start_nr = perform_actions(start_nr)
            cur_mag = magnitude(start_nr)
            if cur_mag > max_mag:
                max_mag = cur_mag
    return print(max_mag)

if __name__ == '__main__':
    main()
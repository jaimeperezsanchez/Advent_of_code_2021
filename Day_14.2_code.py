from collections import Counter, defaultdict
from pprint import pprint

def read_input():
    with open('./Day_14_input.txt', 'r') as f:
        data_str = f.readlines()
    template = data_str[0].strip()
    rules = {x[0]: x[1] for x in (line.strip().split(" -> ") for line in data_str[2:])}
    return template, rules

def main():
    # Read input
    template, rules = read_input()
    n_steps = 40
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i] + template[i+1]] += 1

    for _ in range(n_steps):
        tmp_dict = defaultdict(int)
        for pair, value in pairs.items():
            tmp_dict[pair[0] + rules[pair]] += pairs[pair]
            tmp_dict[rules[pair] + pair[1]] += value
        pairs = tmp_dict

    elements = defaultdict(int)
    for pair, value_ in pairs.items():
        elements[pair[0]] += value_
    elements[template[-1]] += 1

    return print(max(elements.values()) - min(elements.values()))


if __name__ == '__main__':
    main()
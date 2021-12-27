from collections import Counter
from pprint import pprint

def read_input():
    with open('./Day_14_input.txt', 'r') as f:
        data_str = f.readlines()
    template = data_str[0].strip()
    rules = [x.strip().split(' -> ') for x in data_str[2:]]
    return template, rules

def count_rules(template, rule):
    template_list = list(template)
    A, B = rule[0], rule[1]
    n_rule = 0
    for i, letter in enumerate(template_list):
        if letter == B and i > 0:
            if template_list[i-1] == A:
                n_rule += 1
    return n_rule

def main():
    # Read input
    template, rules = read_input()
    n_steps = 10
    for step in range(n_steps):
        rules_applied = []
        # Check what rules are fulfilled
        for rule in rules:
            rule_occurrences = count_rules(template, rule[0])
            if rule_occurrences > 0:
                rules_applied.append([rule[0], rule[1], rule_occurrences])
        # Apply rules
        for j in rules_applied:
            template_reverse = template[::-1]
            template_next_rev = template_reverse.replace(j[0][::-1], j[0][1] + j[1] + j[0][0], j[2])
            template = template_next_rev[::-1]
   
    most_common = Counter(template).most_common()[0][1]
    print(Counter(template).most_common()[0][0], most_common)
    least_common = Counter(template).most_common()[-1][1]
    print(Counter(template).most_common()[-1][0], least_common)
    return print(most_common - least_common)


if __name__ == '__main__':
    main()
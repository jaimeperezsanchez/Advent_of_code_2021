from collections import defaultdict, Counter
from copy import copy

with open('./6_input.txt', 'r') as f:
    data = f.read()

init_counter = Counter([int(x) for x in data.split(',')])
init = defaultdict(int)
for k, v in init_counter.items():
    init[k] = v
days = 256

for i in range(days):
    # We suppose that there are no 0s in the input    
    # Evolve
    day_after = defaultdict(int)
    day_after[0] = init[1]
    day_after[1] = init[2]
    day_after[2] = init[3]
    day_after[3] = init[4]
    day_after[4] = init[5]
    day_after[5] = init[6]
    day_after[6] = init[7] + init[0]
    day_after[7] = init[8]
    day_after[8] = init[0]
    # Update init
    init = copy(day_after)

print(sum(init.values()))
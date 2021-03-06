from statistics import median

with open('./7_input.txt', 'r') as f:
    data = f.read()

init_positions = [int(x) for x in data.split(',')]
# The best position is the median
median_pos = int(median(init_positions))

# How much fuel must they spend to align to that position?
print(sum([abs(i-median_pos) for i in init_positions]))
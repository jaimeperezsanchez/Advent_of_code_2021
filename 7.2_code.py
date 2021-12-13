from statistics import mean

with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\7_input.txt', 'r') as f:
    data = f.read()

init_positions = [int(x) for x in data.split(',')]
# The best position is the mean
mean_pos = int(mean(init_positions))

total_fuel = 0
for pos in init_positions:
    n = abs(pos - mean_pos)
    total_fuel += n*(n+1)//2
    
print(total_fuel)
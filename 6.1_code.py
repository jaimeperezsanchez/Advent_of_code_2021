with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\6_input.txt', 'r') as f:
    data = f.read()

init = [int(x) for x in data.split(',')]
days = 80

for i in range(days):
    # We suppose that there are no 0s in the input
    evolution = [-1] * len(init)
    day_after = [x+y for x,y in zip(init, evolution)]
    number_new_borns = day_after.count(-1)
    new_borns = [8] * number_new_borns
    day_after_no_0s = [x if x != -1 else 6 for x in day_after]
    init = day_after_no_0s + new_borns

print(len(init))
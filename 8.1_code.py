with open('./8_input.txt', 'r') as f:
    data = f.readlines()

counter = 0
for line in data:
    lst_output = line.split("|")[1].split(" ")
    for num in lst_output:
        if len(num.strip()) in [2, 3, 4, 7]:
            counter += 1

print(f'Number of 1s, 4s, 7s, and 8s: {counter}')
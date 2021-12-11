# Read the input file 
with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\3_input.txt', 'r') as f:
    data = f.readlines()

# To simplify we will just sum the 1s and 0s on each position, and check if it's bigger than number_of_lines / 2
half_number_of_lines = len(data)//2  # 500
count_of_1s = []
for i in range(len(data[0].strip())):
    number_of_1s_in_pos = sum(int(line[i]) for line in data)
    count_of_1s.append(number_of_1s_in_pos)

gamma_rate = '0b'
epsilon_rate = '0b'
for n in count_of_1s:
    if n == half_number_of_lines:
        print("Error: Same number of 1s than of 0s")
    if n > half_number_of_lines:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2) 
print(gamma_rate_dec * epsilon_rate_dec)
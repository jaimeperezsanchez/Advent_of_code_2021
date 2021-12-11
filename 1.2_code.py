# Read the input file 
with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\1_input.txt', 'r') as f:
    data = f.readlines()

# Set counter to 0
counter_increases = 0
# Loop the data and check if the next three-sliding window is bigger than the previous
pre_number_list = [int(n) for n in data[:3]]
for i in range(1, len(data)-2):
    post_number_list = [int(n) for n in data[i:i+3]]
    if sum(post_number_list) > sum(pre_number_list):
        counter_increases += 1
    pre_number_list = post_number_list
print(counter_increases)
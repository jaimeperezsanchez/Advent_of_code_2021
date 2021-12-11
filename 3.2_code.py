import copy

with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\3_input.txt', 'r') as f:
    data = f.readlines()

def find_most_common_in_pos(lst, pos):
    half_number_of_lines = len(lst)/2
    number_of_1s = sum(int(line[pos]) for line in lst)
    if number_of_1s == half_number_of_lines:
        return 3
    elif number_of_1s > half_number_of_lines:
        return 1
    else:
        return 0

# Oxygen
indexes_oxygen = list(range(len(data)))
for i in range(len(data[0].strip())):
    filtered_data_oxygen = [data[i] for i in indexes_oxygen]
    most_common = find_most_common_in_pos(filtered_data_oxygen, i) 
    copy_of_indexes_oxygen = copy.deepcopy(indexes_oxygen)
    print(most_common)
    if most_common in [1, 3]:
        for j in copy_of_indexes_oxygen:
            if data[j][i] == '0':
                indexes_oxygen.remove(j)
    else:  # most_common == 0 
        for j in copy_of_indexes_oxygen:
            if data[j][i] == '1':
                indexes_oxygen.remove(j)
    print(len(indexes_oxygen))
    if len(indexes_oxygen) == 1:
        Oxygen = data[indexes_oxygen[0]]
        print(Oxygen)
        break
    if len(indexes_oxygen) == 0:
        print("Error: no coincidences in oxygen")
        break

# CO2
indexes_CO2 = list(range(len(data)))
for i in range(len(data[0].strip())):  
    filtered_data_CO2 = [data[i] for i in indexes_CO2]
    most_common = find_most_common_in_pos(filtered_data_CO2, i) 
    copy_of_indexes_CO2 = copy.deepcopy(indexes_CO2)
    print(most_common)
    if most_common == 0:
        for j in copy_of_indexes_CO2:
            if data[j][i] == '0':
                indexes_CO2.remove(j)
    elif most_common in [1, 3]:
        for j in copy_of_indexes_CO2:
            if data[j][i] == '1':
                indexes_CO2.remove(j)
    print(len(indexes_CO2))
    if len(indexes_CO2) == 1:
        CO2 = data[indexes_CO2[0]]
        print(CO2)
        break
    if len(indexes_CO2) == 0:
        print("Error: no coincidences in CO2")
        break    
    
# Result
Oxygen_dec = int(('0b'+Oxygen), 2)
CO2_dec = int(('0b'+CO2), 2)
print(Oxygen_dec * CO2_dec)


# Read the input file 
with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\2_input.txt', 'r') as f:
    data = f.readlines()

# Set to 0 the positions
Forward_position = 0
Depth_position = 0
Aim = 0

# Loop the data and update the positions
for line in data:
    input_data = line.split()
    action = input_data[0]
    if action == "forward":
        Forward_position += int(input_data[1])
        Depth_position += (Aim * int(input_data[1]))
    elif action == "down":
        Aim += int(input_data[1])
    elif action == "up":
        Aim -= int(input_data[1])
    else:
        print("Error reading the action")

# Multiply the positions to get the final result
print(Forward_position * Depth_position)   
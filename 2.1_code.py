# Read the input file 
with open('./2_input.txt', 'r') as f:
    data = f.readlines()

# Set to 0 the positions
Forward_position = 0
Depth_position = 0

# Loop the data and update the positions
for line in data:
    input_data = line.split()
    action = input_data[0]
    if action == "forward":
        Forward_position += int(input_data[1])
    elif action == "down":
        Depth_position += int(input_data[1])
    elif action == "up":
        Depth_position -= int(input_data[1])
    else:
        print("Error reading the action")

# Multiply the positions to get the final result
print(Forward_position * Depth_position)   
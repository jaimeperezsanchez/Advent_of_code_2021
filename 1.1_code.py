# Read the input file 
with open('./1_input.txt', 'r') as f:
    data = f.readlines()

# Set counter to 0
counter_increases = 0
# Loop the data and check if the next number is bigger than the previous one
pre_number = int(data[0])
for n in data[1:]:
    post_number = int(n)
    if post_number > pre_number:
        counter_increases += 1
    pre_number = post_number
print(counter_increases)
with open('./9_input.txt', 'r') as f:
    data_str = f.readlines()

## Convert lines: str to lists of ints
data_lst = [list(x.strip()) for x in data_str]
data = data_lst.copy()
for i, line in enumerate(data):
    for j, n in enumerate(line):
        data[i][j] = int(n)

## To simplify the operations we will insert values of 9999 around the entire map
border = [9999]*(len(data[0])-2)
# on the top
data.insert(0, border)
# on the bottom
data.append(border)
# on the left and right
for i, line in enumerate(data):
    line.insert(0, 9999)
    line.append(9999)

## Funciton to heck adjacent points and return the lower point position
def check_adjacent_points(x, y):
    lowest = True
    value = data[x][y]
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for neighbor in neighbors:
        i, j = neighbor
        if data[i][j] <= value:
            lowest = False
    return lowest

## Loop the map
lowest_points = []
for i, line in enumerate(data):
    for j, column in enumerate(line):
        if data[i][j] < 10:
            if check_adjacent_points(i, j):
                lowest_points.append([i,j])

total_sum = 0
for point in lowest_points:
    total_sum += data[point[0]][point[1]] + 1

print(total_sum)
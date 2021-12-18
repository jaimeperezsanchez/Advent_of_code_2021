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
def find_lowest_adjacent_point(x, y):
    lowest_i = x
    lowest_j = y
    value = data[x][y]
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for neighbor in neighbors:
        i, j = neighbor
        if data[i][j] < value:
            lowest_i = i
            lowest_j = j
    return lowest_i, lowest_j

## Loop the map
basins = {}
visited_points = set()
for i, line in enumerate(data):
    for j, column in enumerate(line):
        if ((i,j) not in visited_points) and (data[i][j] < 9):
            set_basin = set()
            set_basin.add((i,j))
            visited_points.add((i,j))
            test_i = i
            test_j = j
            low_i, low_j = find_lowest_adjacent_point(test_i, test_j)
            set_basin.add((low_i,low_j))
            visited_points.add((i,j))
            while not(test_i == low_i and test_j == low_j):
                test_i, test_j = low_i, low_j
                low_i, low_j = find_lowest_adjacent_point(test_i, test_j)
                set_basin.add((low_i,low_j))
                visited_points.add((i,j))

            pre_set_basin= basins.get((low_i, low_j)) 
            # If we have already get that lowest point
            if pre_set_basin is not None:
                for p in set_basin:
                    pre_set_basin.add(p)
                basins[(low_i, low_j)] = pre_set_basin
            # If this is the first time we get that lowest point
            else:
                basins[(low_i, low_j)] = set_basin

lens_basins = [len(x) for x in list(basins.values())]
lens_basins.sort()
biggests_bassins = lens_basins[-3:]
result = 1
for v in biggests_bassins:
    result *= v
print(result)
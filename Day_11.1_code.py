import numpy as np

def read_input():
    ### Read input
    with open('./Day_11_input.txt', 'r') as f:
        data_str = f.readlines()
    # Convert lines: str to lists of ints
    data = [list(x.strip()) for x in data_str]
    for i, line in enumerate(data):
        for j, n in enumerate(line):
            data[i][j] = int(n)
    # Return numpy array
    return np.array(data)

def increase_adjacent_points(x, y, data, points_flashed): 
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
    for neighbor in neighbors:
        if neighbor not in points_flashed:
            i, j = neighbor
            if -1 < i < 10 and -1 < j < 10:
                data[i][j] += 1
    return data

def main():
    # Read input
    array_data = read_input()

    # Constants
    array_1s = np.ones(array_data.shape, dtype=int)
    n_steps = 100
    n_flashes = 0
    n_rows = array_data.shape[0]
    n_columns = array_data.shape[1]

    # Loop over steps
    for i in range(n_steps):
        pts_flased = []
        array_next = array_data + array_1s
        any_flash = True
        while any_flash:
            any_flash = False
            for i in range(n_rows):
                for j in range(n_columns):
                    num = array_next[i][j]
                    if num > 9:
                        n_flashes += 1
                        pts_flased.append((i,j))
                        any_flash = True
                        array_next = increase_adjacent_points(i, j, array_next, pts_flased)
                        array_next[i][j] = 0
            if np.amax(array_next) > 9:
                any_flash = True
        array_data = np.copy(array_next)

    return print(n_flashes)

if __name__ == '__main__':
    main()
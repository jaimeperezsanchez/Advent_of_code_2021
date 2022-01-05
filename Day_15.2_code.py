from typing import Any
import numpy as np
import heapq

def read_input():
    with open('./Day_15_input.txt', 'r') as f:
        data_str = f.readlines()
    data = [line.strip() for line in data_str]
    return np.array([[int(x) for x in line] for line in data])
    
def main():
    grid = read_input()
    # expand grid
    column = np.vstack([grid, grid + 1, grid + 2, grid + 3, grid + 4])
    generated_grid = np.hstack([column, column + 1, column + 2, column + 3, column + 4])
    generated_grid[np.where(generated_grid > 9)] -= 9

    node_list = [(0, (0, 0))]
    dist = np.full_like(generated_grid, int(np.sum(generated_grid)))
    dist[0, 0] = 0
    term_node = [x - 1 for x in generated_grid.shape]
    surroundings = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = set()
    while node_list:
        cur_risk, cur_node = heapq.heappop(node_list)
        visited.add(cur_node)
        nbs = [(cur_node[0] + oy, cur_node[1] + ox) for oy, ox in surroundings if
                0 <= cur_node[0] + oy < dist.shape[0] and 0 <= cur_node[1] + ox < dist.shape[1]]
        for nb in nbs:
            if nb not in visited:
                new_dist = dist[cur_node[0], cur_node[1]] + generated_grid[nb[0], nb[1]]
                if new_dist < dist[nb[0], nb[1]]:
                    dist[nb[0], nb[1]] = new_dist
                    heapq.heappush(node_list, (new_dist, nb))
        if cur_node == term_node:
            break
    return print(dist[term_node[0], term_node[1]])

if __name__ == '__main__':
    main()
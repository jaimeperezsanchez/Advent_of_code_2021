import numpy as np
import heapq

def read_input():
    with open('./Day_15_input.txt', 'r') as f:
        data_str = f.readlines()
    data = [line.strip() for line in data_str]
    return np.array([[int(x) for x in line] for line in data])
    
def main():
    grid = read_input()
    node_list = [(0, (0, 0))]
    dist = np.full_like(grid, int(np.sum(grid)))
    dist[0, 0] = 0
    term_node = [x - 1 for x in grid.shape]
    surroundings = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = set()
    while node_list:
        cur_risk, cur_node = heapq.heappop(node_list)
        visited.add(cur_node)
        nbs = [(cur_node[0] + oy, cur_node[1] + ox) for oy, ox in surroundings if
                0 <= cur_node[0] + oy < dist.shape[0] and 0 <= cur_node[1] + ox < dist.shape[1]]
        for nb in nbs:
            if nb not in visited:
                new_dist = dist[cur_node[0], cur_node[1]] + grid[nb[0], nb[1]]
                if new_dist < dist[nb[0], nb[1]]:
                    dist[nb[0], nb[1]] = new_dist
                    heapq.heappush(node_list, (new_dist, nb))
        if cur_node == term_node:
            break
    return print(dist[term_node[0], term_node[1]])

if __name__ == '__main__':
    main()
from collections import defaultdict
from pprint import pprint

def read_input():
    with open('./Day_12_input.txt', 'r') as f:
        data_str = f.readlines()
    return [x.strip().split('-') for x in data_str]

def get_paths_map(map_connections):
    lst_paths = []
    visited = set()
    stack = [['start']]
    small = [x for x in map_connections if x.islower() and x != "end" and x != "start"]
    while stack:
        previous = stack.pop()
        for next_step in map_connections[previous[-1]]:
            if next_step == 'end':
                path = previous.copy()
                path.append(next_step)
                lst_paths.append(path)
            elif next_step.isupper() or next_step not in previous:
                path = previous.copy()
                path.append(next_step)
                stack.append(path)
            elif next_step != 'start' and all(
                previous.count(x) <= 1 for x in previous if x.islower()
            ):
                path = previous.copy()
                path.append(next_step)
                stack.append(path)
    return lst_paths

def main():
    # Read input
    data = read_input()
    
    # Create map of connections
    map_connections = defaultdict(set)
    for line in data:
        map_connections[line[0]].add(line[1])
        map_connections[line[1]].add(line[0])
    
    # Get paths map    
    all_paths = get_paths_map(map_connections)
    print(len(all_paths))


if __name__ == '__main__':
    main()
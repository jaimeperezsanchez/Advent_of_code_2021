import numpy as np
from pprint import pprint

def read_input():
    with open('./Day_13_input.txt', 'r') as f:
        data_str = f.readlines()
    points = []
    folds = []
    for line in data_str:
        if line[0] == 'f':
            f = line.split('=')
            folds.append([f[0][-1], int(f[1])])
        elif line[0] != '\n': 
            coordinate = line.strip().split(',')
            points.append([int(coordinate[0]), int(coordinate[1])])
    return points, folds

def main():
    # Read input
    points, folds = read_input()

    # get size of the paper
    x_max = 0
    y_max = 0
    for fold in folds:
        if fold[0] == 'x' and x_max == 0:
            x_max = fold[1]*2 + 1
        elif fold[0] == 'y' and y_max == 0:
            y_max = fold[1]*2 + 1
    
    # create a matrix and fill it with zeros
    matrix = np.zeros((y_max, x_max), dtype=int)
    # add points to the matrix
    for point in points:
        matrix[point[1], point[0]] = 1
    
    # fold the matrix
    for fold in folds:
        if fold[0] == 'x':
            matrix_aux = np.delete(matrix, fold[1], axis=1)
            A, B = np.split(matrix_aux, 2, axis=1)
            matrix = np.add(A, np.fliplr(B))
            break
        elif fold[0] == 'y':
            matrix_aux = np.delete(matrix, fold[1], axis=0)
            A, B = np.split(matrix_aux, 2, axis=0)
            matrix = np.add(A, np.flipud(B))
            break
    
    # count the number of points
    return print(np.count_nonzero(matrix))

if __name__ == '__main__':
    main()
def read_input():
    with open('./Day_17_input.txt', 'r') as f:
        data_str = f.read()
    x_data = data_str.split('target area: x=')[1].split(', y=')[0]
    x_min, xmax = [int(x) for x in x_data.split('..')]
    y_data = data_str.split('y=')[1]
    y_min, ymax = [int(y) for y in y_data.split('..')]
    return x_min, xmax, y_min, ymax

def main():
    x_min, x_max, y_min, ymax = read_input()
    return print(int(abs(y_min) * (abs(y_min) - 1) / 2))

if __name__ == '__main__':
    main()
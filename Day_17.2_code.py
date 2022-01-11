import math 

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
    vymax = y_min
    vymin = -y_min
    vxmax = x_max
    vxmin = math.ceil((math.sqrt(1 + 8 * x_min) - 1) / 2)
    hits = 0
    for cur_vx in range(vxmin, vxmax + 1):
        for cur_vy in range(vymax, vymin + 1):
            vy = cur_vy
            vx = cur_vx
            pos_x = 0
            pos_y = 0
            while True:
                pos_x += vx
                pos_y += vy
                if vx != 0:
                    vx = vx - 1
                vy -= 1
                # No hit
                if pos_x > x_max or pos_y < y_min:
                    break
                # Hit
                elif x_min <= pos_x <= x_max and y_min <= pos_y <= ymax:
                    hits += 1
                    break
    return print(hits)

if __name__ == '__main__':
    main()
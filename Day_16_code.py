import numpy as np

def read_input():
    with open('./Day_16_input.txt', 'r') as f:
        data_str = f.read().strip()
    data_bin = [bin(int(x, 16))[2:].zfill(4) for x in data_str]
    return "".join(data_bin)

def parse_data(bin_str, idx, ver_sum):
    ver_sum += int(bin_str[idx:idx + 3], 2)
    tp = int(bin_str[idx + 3:idx + 6], 2)
    idx += 6
    if tp == 4:
        not_last = True
        bin_value = ""
        while not_last:
            bin_value += bin_str[idx + 1:idx + 5]
            if bin_str[idx] == "0":
                not_last = False
            idx += 5
        return idx, ver_sum, int(bin_value, 2)
    else:
        expr_values = []
        l_id = bin_str[idx]
        idx += 1
        if l_id == "0":
            length_in_bits = int(bin_str[idx:idx + 15], 2)
            idx += 15
            end_point = idx + length_in_bits
            while idx < end_point:
                idx, ver_sum, expr_value = parse_data(bin_str, idx, ver_sum)
                expr_values.append(expr_value)
        else:
            length_in_subpackets = int(bin_str[idx:idx + 11], 2)
            idx += 11
            for _ in range(length_in_subpackets):
                idx, ver_sum, expr_value = parse_data(bin_str, idx, ver_sum)
                expr_values.append(expr_value)
        if tp == 0:
            return idx, ver_sum, sum(expr_values)
        elif tp == 1:
            res = 1
            for x in expr_values:
                res *= x
            return idx, ver_sum, res
        elif tp == 2:
            return idx, ver_sum, min(expr_values)
        elif tp == 3:
            return idx, ver_sum, max(expr_values)
        elif tp == 5:
            return idx, ver_sum, int(expr_values[0] > expr_values[1])
        elif tp == 6:
            return idx, ver_sum, int(expr_values[0] < expr_values[1])
        elif tp == 7:
            return idx, ver_sum, int(expr_values[0] == expr_values[1])


def main():
    binary_repr = read_input()
    print(parse_data(binary_repr, 0, 0))

if __name__ == '__main__':
    main()
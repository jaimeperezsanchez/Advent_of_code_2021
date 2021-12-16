from itertools import permutations

with open('./8_input.txt', 'r') as f:
    data = f.readlines()

#original_digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
permutations_0 = ["".join(x) for x in list(permutations('abcefg'))]
permutations_1 = ["".join(x) for x in list(permutations('cf'))]
permutations_2 = ["".join(x) for x in list(permutations('acdeg'))]
permutations_3 = ["".join(x) for x in list(permutations('acdfg'))]
permutations_4 = ["".join(x) for x in list(permutations('bcdf'))]
permutations_5 = ["".join(x) for x in list(permutations('abdfg'))]
permutations_6 = ["".join(x) for x in list(permutations('abdefg'))]
permutations_7 = ["".join(x) for x in list(permutations('acf'))]
permutations_8 = ["".join(x) for x in list(permutations('abcdefg'))]
permutations_9 = ["".join(x) for x in list(permutations('abcdfg'))]

total_sum = 0

for line in data:
    encription = {}
    inputs, outs = line.split(" | ")
    lst_inputs = [x.strip() for x in inputs.split(" ")]
    lst_outputs = [y.strip() for y in outs.split(" ")]
    # First get the numbers with unique len()
    for n in lst_inputs:
        if len(n) == 2:
            repr_1 = n
        elif len(n) == 3:
            repr_7 = n
        elif len(n) == 4:
            repr_4 = n
        elif len(n) == 7:
            repr_8 = n
    # Compare the 1 and the 7 to extract "a"
    for letter in repr_7:
        if letter not in repr_1:
            encription[letter] = 'a'
    ### Play with the numbers of len() 6 -> 0, 6, 9 
    nums_len_6 = [n for n in lst_inputs if len(n) == 6]
    # Comparing with 1 we can extract "c" and "f"
    for i, letter in enumerate(repr_1):
        found_c_f = False
        for try_len_6 in nums_len_6:
            if letter not in try_len_6: #we found "c"
                repr_6 = try_len_6
                encription[letter] = 'c'
                c_encripted = letter
                if i == 0:
                    encription[repr_1[1]] = 'f'
                    f_encripted = repr_1[1]
                else:
                    encription[repr_1[0]] = 'f'
                    f_encripted = repr_1[0]
                found_c_f = True
                break
        if found_c_f:
            break
    # Comparing with 4 we can extract "d"
    for i, letter in enumerate(repr_4):
        found_d = False
        # To play just with letters "d"
        if letter not in [c_encripted, f_encripted]:
            for try_len_6 in nums_len_6:
                if letter not in try_len_6: #we found "d"
                    repr_0 = try_len_6
                    encription[letter] = 'd'
                    d_encripted = letter
                    found_d = True
                    break
        if found_d:
            break
    # Extract "b" by discard
    for letter in repr_4:
        if letter not in [c_encripted, f_encripted, d_encripted]:
            encription[letter] = 'b'
    # Comparint 8 with 9 to extract "e" 
    for n in nums_len_6:
        if n not in [repr_0, repr_6]:
            repr_9 = n
            break
    for letter in repr_8:
        if letter not in repr_9:
            encription[letter] = 'e'
            break
    # Extract "g" by discard
    gathered = list(encription.keys())
    for letter in repr_8:
        if letter not in gathered:
            encription[letter] = 'g'
            break
    ### Now decode the output 
    number_output = []
    for n in lst_outputs:
        if len(n) == 2:
            number_output.append(1)
        elif len(n) == 3:
            number_output.append(7)
        elif len(n) == 4:
            number_output.append(4)
        elif len(n) == 7:
            number_output.append(8)
        elif len(n) == 5: # 2 or 3 or 5
            decoded_digit = []
            for letter in n:
                decoded_digit.append(encription.get(letter))
            decoded_digit_join = "".join(decoded_digit)
            if decoded_digit_join in permutations_2:
                number_output.append(2)
            elif decoded_digit_join in permutations_3:
                number_output.append(3)
            elif decoded_digit_join in permutations_5:
                number_output.append(5)
            else:
                print("Error")
        elif len(n) == 6: # 0 or 6 or 9
            decoded_digit = []
            for letter in n:
                decoded_digit.append(encription.get(letter))
            decoded_digit_join = "".join(decoded_digit)
            if decoded_digit_join in permutations_0:
                number_output.append(0)
            elif decoded_digit_join in permutations_6:
                number_output.append(6)
            elif decoded_digit_join in permutations_9:
                number_output.append(9)
            else:
                print("Error")
    sting_ints = [str(x) for x in number_output]
    int_output = int("".join(sting_ints))
    total_sum += int_output
print(total_sum)

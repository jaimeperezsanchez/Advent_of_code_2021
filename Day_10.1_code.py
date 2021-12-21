with open('./Day_10_input.txt', 'r') as f:
    data = f.readlines()

def get_score(line):
    stack = []
    line_lst = list(line.strip())
    for char in line_lst:
        if char in open_chunk:
            stack.append(char)
        elif char in close_chunk:
            open_char = open_chunk[close_chunk.index(char)]
            if stack and stack[-1] == open_char:
                stack.pop()
            else:
                if char == ')':
                    return 3
                elif char == ']':
                    return 57
                elif char == '}':
                    return 1197
                elif char == '>':
                    return 25137
    if not stack:
        # Empty list
        return 0
    else:
        # Incomplete sequences
        return 0

## Scores
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points

def main():
    total_score = sum(get_score(line) for line in data)
    print(total_score)

if __name__ == '__main__':
    open_chunk = '([{<'
    close_chunk = ')]}>'
    main()
    
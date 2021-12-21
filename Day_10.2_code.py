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
                # Corrupted sequences
                return 0
    if not stack:
        # Empty list
        return 0
    else:
        # Incomplete sequences
        reversed_stack = stack[::-1]
        closing_chars = []
        for char in reversed_stack:
            closing_chars.append(close_chunk[open_chunk.index(char)])
        score = 0
        for char in closing_chars:
            score *= 5
            score += close_chunk.index(char) + 1
        return score

def main():
    scores_lst = [get_score(line) for line in data if get_score(line) != 0]
    scores_sorted = sorted(scores_lst)
    print(scores_sorted[int(len(scores_sorted)/2)])

if __name__ == '__main__':
    open_chunk = '([{<'
    close_chunk = ')]}>'
    main()
    
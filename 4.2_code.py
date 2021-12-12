with open(r'C:\Users\jperezs\OneDrive - Universidad Pontificia Comillas\Documentos\Python Scripts\Advent_of_code_2021\4_input.txt', 'r') as f:
    data = f.readlines()

# Parse the numbers
numbers = [int(x) for x in data[0].split(',')]
# Parse the boards
boards = []
for i, line in enumerate(data[1:]):
    if i % 6 == 0:  # new board
        if i != 0:
            boards.append(aux_board)
        aux_board = []
    else:
        aux_board.append([int(x) for x in line.split()])
        if i == len(data[1:]) - 1:
            boards.append(aux_board)

# Check if there is a winner
def check_winner(checked_board):
    # Check rows
    for row in checked_board:
        if all(x == -1 for x in row):
            return True
    # Check columns by transposing the board
    board_transposed = (list(map(list, zip(*checked_board))))
    for row in board_transposed:
        if all(x == -1 for x in row):
            return True
    return False

# Change -1s to 0s
def change_numbers(board):
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == -1:
                board[i][j] = 0
    return board

# Play Bingo
def play_bingo(numbers, boards):
    index_boards = list(range(len(boards)))
    for n in numbers:
        for idx, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, num in enumerate(row):
                    if num == n:
                        # If the number is in the board, replace it with -1
                        board[i][j] = -1
                        if check_winner(board):
                            if len(index_boards) == 1 and idx == index_boards[0]:
                                last_winner = boards[index_boards[0]]
                                print(last_winner)
                                new_board = change_numbers(last_winner)
                                from itertools import chain
                                Sum_board = sum(list(chain.from_iterable(new_board)))
                                return  print(Sum_board * n)
                            else:
                                try:
                                    index_boards.remove(idx)
                                except ValueError:
                                    pass
    return print('No winner')

play_bingo(numbers, boards)
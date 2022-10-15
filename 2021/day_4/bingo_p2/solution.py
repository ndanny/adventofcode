# https://adventofcode.com/2021/day/4

from tabnanny import check


f = open('2021/day_4/input.txt', 'r')
inp = f.readlines()

boards = []
nums = [int(num) for num in inp[0].split(',')]

# Read input and construct a list of all 2D boards
current_board = []
for i in range(2, len(inp)):
    if inp[i] == '\n':
        boards.append(current_board)
        current_board = []
    else:
        row = []
        for num in inp[i].strip('\n').split(' '):
            if num.isdigit():
                row.append(int(num))

        current_board.append(row)

if current_board:
    boards.append(current_board)

f.close()

# Iterate through all the numbers and calculate until we find the winning board

# Helper function to mark boards
def mark_boards(boards, called_num):
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == called_num:
                    boards[i][j][k] = 'X'

# Checks if the board wins or not
def check_board(board) -> bool:
    for i in range(5):
        # check if entire row is marked
        row_match = True
        for j in range(5):
            if board[i][j] != 'X':
                row_match = False
                break
        if row_match:
            return True
        
        # check if entire column is marked
        col_match = True
        for j in range(5):
            if board[j][i] != 'X':
                col_match = False
                break
        if col_match:
            return True
        
        # check for the diagonal - not needed for this challenge

    return False

non_winning_board_indices = {i for i in range(len(boards))}
last_to_win = None
last_n = None

for n in nums:
    # Track last number called
    last_n = n

    # Everybody mark their boards
    mark_boards(boards, n)

    # Check all non_winning_boards
    winners = set()
    for i in non_winning_board_indices:
        board = boards[i]
        if len(winners) == len(non_winning_board_indices):
            break
        if check_board(board):
            winners.add(i)
            last_to_win = board

    non_winning_board_indices = non_winning_board_indices - winners

    # Break out if there is only 1 non winning board left
    if len(non_winning_board_indices) == 0:
        break
    
print(last_to_win)
print(last_n)

result = 0
for i in range(len(last_to_win)):
    for j in range(len(last_to_win[0])):
        if type(last_to_win[i][j]) == int:
            result += last_to_win[i][j]

result *= last_n
print(result)

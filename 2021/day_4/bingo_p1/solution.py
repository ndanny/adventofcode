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

winning_board = None
last_n = None
for n in nums:
    # Track last number called
    last_n = n

    # Everybody mark their boards
    mark_boards(boards, n)

    # If winning board is found
    for b in boards:
        if check_board(b):
            winning_board = b
            break
    
    # Calculate score
    if winning_board:
        break

for b in winning_board:
    print(b)

print(last_n)

result = 0
for i in range(len(winning_board[0])):
    for j in range(len(winning_board)):
        if type(winning_board[i][j]) == int:
            result += winning_board[i][j]

result *= last_n
print(result)

# Hindsight: in the beginning we don't really need to convert the string int to an actual int

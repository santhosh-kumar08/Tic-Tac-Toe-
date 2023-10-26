# Initialize the board
board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def print_board(board):
    print(' | '.join(board[:3]))
    print('-' * 9)
    print(' | '.join(board[3:6]))
    print('-' * 9)
    print(' | '.join(board[6:9]))

# Function to check if someone has won
def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Main game loop
player = 'X'
while True:
    print_board(board)
    try:
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] != ' ':
            raise ValueError
    except (ValueError, IndexError):
        print("Invalid move. Try again.")
        continue
    board[move] = player
    if check_win(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        break
    if ' ' not in board:
        print_board(board)
        print("It's a draw!")
        break
    player = 'O' if player == 'X' else 'X'

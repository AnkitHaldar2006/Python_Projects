def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 1 to 9.")

def play_game():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
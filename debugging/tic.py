#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9) # Increased from 5 to 9 to perfectly match the board width

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    # If there are any empty spaces left, it's not a draw
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # 1. Error Handling: Catch non-integer text inputs
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue
            
        # 2. Error Handling: Catch numbers outside the 0-2 range
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("\nOut of bounds! Please only enter 0, 1, or 2.\n")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for a winner BEFORE swapping the player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            # Check for a draw if the board is full
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
                
            # Swap players only after a successful, non-game-ending turn
            player = "O" if player == "X" else "X"
            print("\n") # Add spacing for readability
            
        else:
            print("\nThat spot is already taken! Try again.\n")

if __name__ == "__main__":
    tic_tac_toe()
    
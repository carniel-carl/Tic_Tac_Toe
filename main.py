from logo import logo

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

winner = None
game_on = True

print(f"{logo}\n Welcome to my tic tac toe game(X/O).")


def show_board():
    for row in range(len(board)):
        print("\n+---+---+---+")
        print("|", end="")
        for col in range(len(board)):
            print("", board[row][col], end=" |")
    print("\n+---+---+---+")


show_board()

# TODO 1: Create a board.
# TODO 2: Display/show the board.
# TODO 3: Play the game.
# TODO 4: Handle turns and flip the players.
# TODO 5: Check wins ( check rows, columns, diagonal).
# TODO 6: Check tie/draw.

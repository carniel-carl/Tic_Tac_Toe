from logo import logo

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(f"{logo}\n Welcome to my tic tac toe game(X/O).")


def show_board():
    for row in range(len(board)):
        print("\n+---+---+---+")
        print("|", end="")
        for col in range(len(board)):
            print("", board[row][col], end=" |")
    print("\n+---+---+---+")


winner = None
game_on = True
turn_counter = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def edit_board(choice, turn):
    for i in range(1, 10):
        if choice == i:
            if i <= 3:
                board[0][i - 1] = turn
            elif i <= 6:
                num = 4
                board[1][i - num] = turn
                num += 1
            else:
                num = 7
                board[2][i - num] = turn
                num += 1


def play_game():
    global turn_counter

    while game_on:
        # Turn switcher
        if turn_counter % 2 == 0:
            show_board()
            turn = "X"
            choice = int(input(f"{turn} turn.\nSelect a number from 1 - 9: "))
            if choice >= 1 or choice <= 9:
                if choice in numbers:
                    edit_board(choice, turn)
                    numbers.remove(choice)
                    turn_counter += 1
                else:
                    print("Spot already chosen")
            else:
                print("Enter a valid number")
        else:
            show_board()
            turn = "O"
            choice = int(input(f"{turn} turn.\nSelect a number from 1 - 9: "))
            if choice >= 1 or choice <= 9:
                if choice in numbers:
                    edit_board(choice, turn)
                    numbers.remove(choice)
                    turn_counter += 1
                else:
                    print("Spot already chosen")
            else:
                print("Enter a valid number")


play_game()

# TODO 1: Create a board.
# TODO 2: Display/show the board.
# TODO 3: Play the game.
# TODO 4: Handle turns and flip the players.
# TODO 5: Check wins ( check rows, columns, diagonal).
# TODO 6: Check tie/draw.

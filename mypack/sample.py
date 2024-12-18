'''def sayHello():
    print("Hello")

class sample:
    def samp1(self):
        print("Sample")


'''
#NEW CODE CHanged
print("ready for the game😎")
def game(board):
    for row in board:
        print(" | ".join(row))

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def tickgame():
    board = [[" " for _ in range(3)] for _ in range(3)]
    i = ["X", "O"]
    p = 0

    while True:
        game(board)
        print(f"Player {i[p]}: Enter X or O? (row and column):")
        row, col = map(int, input().split())

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = i[p]
            a = winner(board)
            if a:
                game(board)
                print(f"Player {a} wins!👌😍")
                break
            if all(cell != " " for row in board for cell in row):
                game(board)
                print("It's a draw!😒")
                break
            p = 1 - p
        else:
            print("Invalid move. Try again.😢😢")
tickgame()
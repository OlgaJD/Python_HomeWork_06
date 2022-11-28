board =  [[" ", "1", "2", "3"],
          ["1", "-", "-", "-"],
          ["2", "-", "-", "-"],
          ["3", "-", "-", "-"]]

def print_board():
    for x in board:
        print(x[0], x[1], x[2], x[3])

def step_x():
    print("Ход игрока - X")
    line = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while line < 1 or line > 3 or column < 1 or column > 3 or board[line][column] == 'X' or board[line][column] == '0':
        line = int(input("Введите номер строки верно: "))
        column = int(input("Введите номер столбца верно: "))

    board[line][column] = "X"

def step_0():
    print("Ход игрока - 0")
    line = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while line < 1 or line > 3 or column < 1 or column > 3 or board[line][column] == 'X' or board[line][column] == '0':
        line = int(input("Введите номер строки верно: "))
        column = int(input("Введите номер столбца верно: "))

    board[line][column] = "0"

def check_win():
    for x in board:
        if x[1] == x[2] == x[3] != "-":
            print("Победил игрок - ", x[1])
            victory[0] = 1
            break
    for i in range(1, 3):
        if board[1][i] == board[2][i] == board[3][i] != "-":
            print("Победил игрок -", board[1][i])
            victory[0] = 1
            break
    if board[1][1] == board[2][2] == board[3][3] != "-":
        print("Победил игрок -", board[1][1])
        victory[0] = 1

    elif board[1][3] == board[2][2] == board[3][1] != "-":
        print("Победил игрок -", board[1][3])
        victory[0] = 1



print_board()
k = 0
victory = [0]
while True:
    step_x()
    k += 1
    print_board()
    check_win()
    if victory[0] == 1:
        break
    elif k == 9:
        print("Ничья")
        break
    step_0()
    check_win()
    if victory[0] == 1:
        break
    k += 1
    print_board()
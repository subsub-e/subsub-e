import random
def create_board():
    seed = [1, 2, 3, 4, 5, 6]
    random.shuffle(seed)
    x = [[], [], [], [], [], []]
    x[0] += seed
    x[1] += [seed[3], seed[4], seed[5], seed[0], seed[1], seed[2]]
    x[2] += [seed[2], seed[0], seed[1], seed[5], seed[3], seed[4]]
    x[3] += [seed[5], seed[3], seed[4], seed[2], seed[0], seed[1]]
    x[4] += [seed[1], seed[2], seed[0], seed[4], seed[5], seed[3]]
    x[5] += [seed[4], seed[5], seed[3], seed[1], seed[2], seed[0]]
    return x
def shuffle_ribbons(board):
    top_half = board[:3]
    random.shuffle(top_half)
    bottom_half = board[3:]
    random.shuffle(bottom_half)
    return top_half + bottom_half
def shuffle_ribbons2(board):
    top = board[:2]
    random.shuffle(top)
    mid = board[2:4]
    random.shuffle(mid)
    bottom = board[4:]
    random.shuffle(bottom)
    return top + mid + bottom
def transpose(board):
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        transposed[0].append(row[0])
        transposed[1].append(row[1])
        transposed[2].append(row[2])
        transposed[3].append(row[3])
        transposed[4].append(row[4])
        transposed[5].append(row[5])
    return transposed
def create_solution_board():
    board = create_board()
    board = shuffle_ribbons2(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board
def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상", "중", "하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == "하":
        return 10
    if level == "중":
        return 13
    if level == "상":
        return 16
def copy_board(board):
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone
def make_holes(board, no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0, len(board) - 1)
        j = random.randint(0, len(board) - 1)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
            holeset.add((i, j))
    return (board, holeset)
def show_board(board):
    print()
    print('S', '|', '1', '2', '3', '4', '5', '6')
    print('-', '+', '-', '-', '-', '-', '-', '-')
    i = 1
    for row in board:
        for j in range(0, len(row)):
            if row[j] == 0:
                row[j] = '.'
        print(i, '|', row[0], row[1], row[2], row[3], row[4], row[5])
        i += 1
    print()
def get_integer(message, i, j):
    number = input(message)
    while not (i <= int(number) <= j):
        number = input(message)
    return int(number)
def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    return "잘 하셨습니다. 또 들려주세요."
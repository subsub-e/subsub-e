import turtle
import random

def setWorld():
    turtle.setworldcoordinates(-100, -100, 100, 100)
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(-75, -75)

def drawGrid():
    for i in range(2):
        turtle.fd(150)
        turtle.lt(90)
        turtle.fd(150)
        turtle.lt(90)


def drawSquare():
    for i in range(2):
        turtle.fd(37.5)
        turtle.lt(90)
        turtle.fd(37.5)
        turtle.lt(90)


def move_turtle():
    turtle.pd()
    while not (turtle.xcor() >= 75):
        drawSquare()
        turtle.setx(turtle.xcor() + 37.5)

def make_box():
    row_boxes = 0
    turtle.sety(-37.5)
    while row_boxes != 4:
        move_turtle()
        turtle.setx(-75)
        turtle.sety(
            turtle.ycor() + 37.5)  
        row_boxes += 1
    turtle.pu()


def labelGrid():
    rows = ['A', 'B', 'C', 'D']
    cols = ['1', '2', '3', '4']

    for row_name in rows:
        turtle.write(row_name, move=False, align='left', font=('Georgia', 40, 'normal'))
        turtle.sety(turtle.ycor() - 40)

    turtle.goto(-65, 75)
    for col_name in cols:
        turtle.write(col_name, move=False, align='left', font=('Georgia', 40, 'normal'))
        turtle.setx(turtle.xcor() + 40)


def eraseEntry(puzzle):
    '''
    Takes in the puzzle
    Asks the user if they want to erase the entry before hand
    '''
    eraser = turtle.Turtle()
    eraser.hideturtle()
    eraser.speed(0)
    eraser.pu()

    ask_user = turtle.textinput('', 'Do you want to erase the previous entry? (y/n)')
    if ask_user in ['y', 'YES', 'yes']:
        eraser.goto(turtle.xcor() + 5,
                    turtle.ycor())  
        eraser.pd()  
        eraser.color('white', 'white')
        eraser.begin_fill()
        eraser.circle(10)
        eraser.end_fill()


def take_input(puzzle):
    grid_rows = ['A', 'B', 'C', 'D']
    grid_cols = ['1', '2', '3', '4']

    col_increment_size = [-60, -30, 10, 50]
    row_increment_size = [50, 10, -30, -60]

    user_input = turtle.textinput('', 'Enter Row and Column (e.g B4)')

    x_cor = 0
    y_cor = 0

    for r in range(0, len(grid_rows)):
        if grid_rows[r] == user_input[0]:  
            y_cor = row_increment_size[r]

    for c in range(0, len(grid_cols)):
        if grid_cols[c] == user_input[1]:  
            x_cor = col_increment_size[c]

    turtle.goto(x_cor, y_cor)


    get_input = turtle.textinput('', 'Enter a number and make your move!')

    for i in range(0, len(grid_rows)):
        if user_input[0] == grid_rows[i]:
            for j in range(0, len(grid_cols)):
                if user_input[1] == grid_cols[j]:
                    if puzzle[i][j] != 0:
                        eraseEntry(puzzle)
                    puzzle[i][j] = int(get_input)
                    make_move = turtle.write(get_input, move=False, align='left', font=('Arial', 35, 'normal'))

    return puzzle


def populatePuzzle(puzzle):
    '''
    Takes in a puzzle (which is a nested list)
    Returns the grid with the initial numbers inside
    '''

    col_increment_size = [-60, -30, 10, 50] 
    row_increment_size = [50, 10, -30, -60]

    for row in range(0, len(puzzle)):
        for col in range(0, len(puzzle[row])):  
            if puzzle[row][col] != 0:
                turtle.goto(col_increment_size[col], row_increment_size[row])
                turtle.write(puzzle[row][col], move=False, align='left', font=('Arial', 35, 'normal'))


def row_check(puzzle):
    '''
    Assumes that puzzle is a nested list
    Returns True if every element in the row is unique
    '''

    check = 0
    for row in range(0, len(puzzle)):
        if len(puzzle[row]) == len(set(puzzle[row])) and 0 not in puzzle[
            row]:  
            check += 1  
    if check == 4:
        return True

    else:
        return 'Keep trying!'


def col_check(puzzle):
    '''
    Assumes that puzzle is a nested list
    Returns True if every element in the column is unique
    '''

    col_1 = [s[0] for s in puzzle]  
    col_2 = [s[1] for s in puzzle]  
    col_3 = [s[2] for s in puzzle]  
    col_4 = [s[3] for s in puzzle]  
    all_col = [col_1, col_2, col_3, col_4]  

    check = 0
    for col in range(0, len(all_col)):
        if len(all_col[col]) == len(set(puzzle[col])) and 0 not in all_col:
            check += 1

    if check == 4:  
        return True

    else:
        return 'Keep trying!'


def box_check(puzzle):
    '''
    Assumes that puzzle is a nested list
    Rearragnes the puzzle so that each 'row' is a box.
    '''

    box_1 = [s[0:2] for s in puzzle[0:2]]  
    box_2 = [s[2:] for s in puzzle[0:2]]
    box_3 = [s[0:2] for s in puzzle[2:]]
    box_4 = [s[2:] for s in puzzle[2:]]

    all_box = [box_1, box_2, box_3, box_4]

    check = 0

    for box in all_box:
        if len(box[0] + box[1]) == len(set(box[0] + box[1])) and 0 not in box[0] + box[1]:
            check += 1

    if check == 4:
        return True


    else:
        return 'Keep trying!'



def isboardfilled(puzzle):
    '''
    Assumes puzzle is a nested list
    Returns True if the number of 'non_zero' elements match the puzzle
    '''

    non_zero = []
    for row in range(len(puzzle)):
        for el in range(len(puzzle[row])):
            if puzzle[row][el] != 0:
                non_zero.append(puzzle[row][el])
                if len(non_zero) == len(puzzle[row]) * len(
                        puzzle):  
                    return True  

def replay():
    return turtle.textinput('', "Do you want to play again? (y/n)") in ['yes', 'y', "YES"]


puzzle_1 = [[3, 4, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0],
            [4, 2, 3, 1]]  
puzzle_2 = [[4, 0, 0, 1], [0, 1, 3, 0], [0, 4, 1, 0],
            [1, 0, 0, 3]]  
puzzle_3 = [[0, 0, 0, 0], [2, 3, 4, 1], [3, 4, 1, 2],
            [0, 0, 0, 0]]
puzzle_4 = [[0, 2, 4, 0], [1, 0, 0, 3], [4, 0, 0, 2],
            [0, 1, 3, 0]]
puzzle_5 = [[0, 4, 2, 0], [2, 0, 0, 0], [0, 0, 0, 3],
            [0, 3, 1, 0]]

all_puzzles = [puzzle_1, puzzle_2, puzzle_3, puzzle_4, puzzle_5]

def start():
    while True:
        turtle.reset()  
        setWorld()
        game_won = False
        turtle.pd()
        drawGrid()
    
        turtle.pu()
        turtle.goto(-75, 0)
        turtle.pd()
        turtle.fd(150)
        turtle.pu()
        turtle.goto(0, 75)
        turtle.lt(270)
        turtle.pd()
        turtle.fd(150)
        turtle.pu()
        turtle.goto(-75, -75)

        turtle.pensize(2)
        make_box()
        turtle.goto(-95, 45)  
        labelGrid()
        game_puzzle = all_puzzles[random.randint(0, 4)] 
        populatePuzzle(game_puzzle)

        while game_won != True:
            take_input(game_puzzle)

            if isboardfilled(game_puzzle):
                confirm_sol = turtle.textinput('', 'Are you sure you want to submit this solution? (y/n)')
                if confirm_sol in ['yes', 'y', 'YES']:
                    if row_check(game_puzzle) == col_check(game_puzzle) == box_check(game_puzzle) == True:
                        turtle.textinput('', 'Congratulations you have won! (Press any key to continue)')
                        game_won = True
                    else:
                         turtle.textinput('', "Your solution is incorrect. Keep trying! (Press any key to continue)")

        if not replay():
            break


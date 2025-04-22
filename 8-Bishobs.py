import time , os
os.system('cls'); print("\n"*2)
n = int(input("Enter the size of the board : ")); print("\n"*2)
board = [[' .' for _ in range(n)] for _ in range(n)]


def safe(row, col):  # check row
    for j in range(col):
        if board[row][j] == ' ∎':
            return False

    for i in range(1, col + 1):  # check original diameters
        r = row - i; c = col - i
        if r >= 0 and c >= 0:
            if board[r][c] == ' ∎':
                return False

    for i in range(1, col + 1):  # check not original diameters
        r = row + i; c = col - i
        if r < n and c >= 0:
            if board[r][c] == ' ∎':
                return False
    return True


def show():  # showing the  board in reall time
    os.system('cls'); print("\n"*4)
    for r in board:
        for j in r:
            print(j, end='      ')
        print("\n"*2)
    time.sleep(0.5)


def solve(col):
    if col == n:
        return True
        
    for row in range(n):  # checking eche col for best row
        board[row][col] = ' ?'; show();  board[row][col] = ' .'  # show tring
        if safe(row, col):
            board[row][col] = ' ∎' ; show()
            if solve(col + 1):  #going for the next col
                return True
            board[row][col] = ' .' ; show() # Deleting the Bishobs for back tracking
    return False
    
solve(0) #start this shitt show whit col 0

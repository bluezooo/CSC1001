def check(row, col):
    #colomn
    for a in range(row):
        if col - 1 - a < 0:
            break
        if queens[row - 1 - a][col - 1 - a] == 1:
            return False
    #row
    for a in range(8):
        if queens[a][col] == 1:
            return False 
    #two diagonals
    for a in range(row):
        if col + 1 + a > 7:
            break
        if queens[row - 1 - a][col + 1 + a] == 1:
            return False
    return True

# row by row
def put_queen(row):
    #Print a valid board
    if row > 7:
        for a in range(8):
            for b in range(8):
                if(queens[a][b] == 1):
                    print('|' + ' |' * b + 'Q|' + ' |' * (7 - b))
        exit()
    ##row by row to put the queens. 
    ##if no places can be put, then return to the last row 
    for a in range(8):
        if check(row, a):
            queens[row][a] = 1
            put_queen(row + 1)
            queens[row][a] = 0

queens = [[0 for _ in range(8)] for _ in range(8)]
put_queen(0)

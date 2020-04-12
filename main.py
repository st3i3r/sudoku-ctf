import pwn
import base64
import time


def google_ctf():
    cipher_text = "Z3JhbmRfbWFzc2l2ID1bCiczMDYzNjM2MjZDNjE2NjZDNjE2MzZDNjE3MjZBNjE2NzZBNkInLAonNjM2MTZDNjE2QTZDNjE2MTY3NjI2QTcyNkI2QzY2MzA2MzYzJywKJzMwMzAzMDY2NzU3NTczNzM2QzY2NkM2QjZFNzM2NzMwNjM2MycsCidDNjY2NTYzNjE2NTY4Njg3MjY1NzIzMDYzNjM2RDY1NjM2RDYnLAonMzEyRjM0NTc2ODY1NkUyMDY0Njk2NDIwNzQ2ODY1MjAyMDIwJywKJzc1MjAzMDYzNjM2NjIwNjY2OTI3NkQ3NDY5NzIyMDY1MjA2NCcsCic2QzZGNjg2QzZGNjMwNjM2Mzg2QzZGNjg2QzZGNjg2QzZGNjgnLAonMzA2MzYzNjI2QzYxNjY2QzYxNjM2QzYxNzI2QTYxNjc2QTZCJywKJzYzNjE2QzYxNkE2QzYxNjE2NzYyNkE3MjZCNkM2NjMwNjM2MycsCiczMDMwMzA2Njc1NzU3MzczNkM2NjZDNkI2RTczNjczMDYzNjMnLAonMzA2MzYzNzU3NTczNzM2QzYxNkE2QzYxNjE2NzYyNjZFNzZCJywKJzYyNzI2NTY1MzM3MjY1NjUzMzMzMzMzMzMzNjQyMDMwNjM2MycsCiczMDYzNjMyMDIwNzU2NjY2NjkyNzZENzQ2OTcyNjU2NDIwMjAnLAonNkM2RjY4NkM2RjYzMDYzNjM4NkM2RjY4NkM2RjY4NkM2RjY4JywKJzYyNzUzMDYzNjM3NDIwNzk2Rjc1MjA2OTczMjA2QzZGNkY3MycsCic2MzY4NjU3MjYzNjg2NTcyNkM2MTMwNjM2MzY2NjU2RDZENjUnLAonNjE2NTY4Njg3MjY1MzA2MzYzNzI2RDY1NjM2RDZDNjY2NTYzJywKJzMyMkYzNDY2Njk3MjczNzQyMDY3NkY2RjY3NkM2NTIwMjAyMCcsCiczMDYzNjM2MjZDNjE2NjZDNjE2MzZDNjE3MjZBNjE2NzZBNkInLAonMzAzMDMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3MzA2MzYzJywKJzMwNjM2Mzc1NzU3MzczNkM2MTZBNkM2MTYxNjc2MjY2RTc2QicsCic2MjcyNjU2NTMzNzI2NTY1MzMzMzMzMzMzMzY0MjAzMDYzNjMnLAonMzA2MzYzMjAyMDc1NjY2NjY5Mjc2RDc0Njk3MjY1NjQyMDIwJywKJzZDNkY2ODZDNkY2MzA2MzYzODZDNkY2ODZDNkY2ODZDNkY2OCcsCic2Mjc1MzA2MzYzNzQyMDc5NkY3NTIwNjk3MzIwNkM2RjZGNzMnLAonNjM2ODY1NzI2MzY4NjU3MjZDNjEzMDYzNjM2NjY1NkQ2RDY1JywKJzYxNjU2ODY4NzI2NTMwNjM2MzcyNkQ2NTYzNkQ2QzY2NjU2MycsCic2MzYxNkM2MTZBNkM2MTYxNjc2MjZBNzI2QjZDNjYzMDYzNjMnLAonMzAzMDMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3MzA2MzYzJywKJ0M2NjY1NjM2MTY1Njg2ODcyNjU3MjMwNjM2MzZENjU2MzZENicsCic3NTIwMzA2MzYzNjYyMDY2NjkyNzZENzQ2OTcyMjA2NTIwNjQnLAonQzY2NjU2MzYxNjU2ODY4NzI2NTcyMzA2MzYzNkQ2NTYzNkQ2JywKJzMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3NkI2NDMwNjM2MycsCic2MzY4NjU3MjYzNjg2NTcyNkM2MTMwNjM2MzY2NjU2RDZENjUnLAonMzAzMDMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3MzA2MzYzJywKJzc1MjAzMDYzNjM2NjIwNjY2OTI3NkQ3NDY5NzIyMDY1MjA2NCcsCic3NTIwMzA2MzYzNjYyMDY2NjkyNzZENzQ2OTcyMjA2NTIwNjQnLAonMzA2MzYzNjI2QzYxNjY2QzYxNjM2QzYxNzI2QTYxNjc2QTZCJywKJzYzNjE2QzYxNkE2QzYxNjE2NzYyNkE3MjZCNkM2NjMwNjM2MycsCiczMDMwMzA2Njc1NzU3MzczNkM2NjZDNkI2RTczNjczMDYzNjMnLAonNTc1NzM3MzZDMzAzMDMwNjY3NjY2QzZCNkU3MzY3MzA2MzYzJywKJzYzNjE2QzYxNkE2QzYxNjE2NzYyNkE3MjZCNkM2NjMwNjM2MycsCic3NTIwMzA2MzYzNjYyMDY2NjkyNzZENzQ2OTcyMjA2NTIwNjQnLAonMzA2Njc1NzU3MzczNkM2NjZDNkI2RTczNjc2QjY0MzA2MzYzJywKJzMwMzAzMDY2NzU3NTczNzM2QzY2NkM2QjZFNzM2NzMwNjM2MycsCiczMDYzNjM3NTc1NzM3MzZDNjE2QTZDNjE2MTY3NjI2NkU3NkInLAonNjI3MjY1NjUzMzcyNjU2NTMzMzMzMzMzMzM2NDIwMzA2MzYzJywKJzMwNjM2MzIwMjA3NTY2NjY2OTI3NkQ3NDY5NzI2NTY0MjAyMCcsCic2QzZGNjg2QzZGNjMwNjM2Mzg2QzZGNjg2QzZGNjg2QzZGNjgnLAonNjI3NTMwNjM2Mzc0MjA3OTZGNzUyMDY5NzMyMDZDNkY2RjczJywKJzYzNjg2NTcyNjM2ODY1NzI2QzYxMzA2MzYzNjY2NTZENkQ2NScsCic2MTY1Njg2ODcyNjUzMDYzNjM3MjZENjU2MzZENkM2NjY1NjMnLAonNTc1NzM3MzZDMzAzMDMwNjY3NjY2QzZCNkU3MzY3MzA2MzYzJywKJzMzMkYzNDYzNzQ2NjIwNzQ2MTZCNjUyMDcwNkM2MTYzNjUzRicsCic2QzZGNjg2QzZGNjMwNjM2Mzg2QzZGNjg2QzZGNjg2QzZGNjgnLAonQzY2NjU2MzYxNjU2ODY4NzI2NTcyMzA2MzYzNkQ2NTYzNkQ2JywKJzMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3NkI2NDMwNjM2MycsCiczMDYzNjM2MjZDNjE2NjZDNjE2MzZDNjE3MjZBNjE2NzZBNkInLAonNjM2MTZDNjE2QTZDNjE2MTY3NjI2QTcyNkI2QzY2MzA2MzYzJywKJzMwMzAzMDY2NzU3NTczNzM2QzY2NkM2QjZFNzM2NzMwNjM2MycsCidDNjY2NTYzNjE2NTY4Njg3MjY1NzIzMDYzNjM2RDY1NjM2RDYnLAonNzUyMDMwNjM2MzY2MjA2NjY5Mjc2RDc0Njk3MjIwNjUyMDY0JywKJzYyNzUzMDYzNjM3NDIwNzk2Rjc1MjA2OTczMjA2QzZGNkY3MycsCic2MzY4NjU3MjYzNjg2NTcyNkM2MTMwNjM2MzY2NjU2RDZENjUnLAonNjE2NTY4Njg3MjY1MzA2MzYzNzI2RDY1NjM2RDZDNjY2NTYzJywKJzYyNzI2NTY1MzM3MjY1NjUzMzMzMzMzMzMzNjQyMDMwNjM2MycsCiczNDJGMzQ2MTZFNzM3NzY1NzIyMDY5NzMyMDc5NjU2MTcyMjAnLAonQzY2NjU2MzYxNjU2ODY4NzI2NTcyMzA2MzYzNkQ2NTYzNkQ2JywKJzMwNjM2MzYyNkM2MTY2NkM2MTYzNkM2MTcyNkE2MTY3NkE2QicsCic2MzYxNkM2MTZBNkM2MTYxNjc2MjZBNzI2QjZDNjYzMDYzNjMnLAonMzA2MzYzNjI2QzYxNjY2QzYxNjM2QzYxNzI2QTYxNjc2QTZCJywKJzYzNjE2QzYxNkE2QzYxNjE2NzYyNkE3MjZCNkM2NjMwNjM2MycsCiczMDMwMzA2Njc1NzU3MzczNkM2NjZDNkI2RTczNjczMDYzNjMnLAonQzY2NjU2MzYxNjU2ODY4NzI2NTcyMzA2MzYzNkQ2NTYzNkQ2JywKJzc1MjAzMDYzNjM2NjIwNjY2OTI3NkQ3NDY5NzIyMDY1MjA2NCcsCiczMDMwMzA2Njc1NzU3MzczNkM2NjZDNkI2RTczNjczMDYzNjMnLAonMzA2MzYzNzU3NTczNzM2QzYxNkE2QzYxNjE2NzYyNjZFNzZCJywKJzYyNzI2NTY1MzM3MjY1NjUzMzMzMzMzMzMzNjQyMDMwNjM2MycsCiczMDYzNjMyMDIwNzU2NjY2NjkyNzZENzQ2OTcyNjU2NDIwMjAnLAonNkM2RjY4NkM2RjYzMDYzNjM4NkM2RjY4NkM2RjY4NkM2RjY4JywKJzYyNzUzMDYzNjM3NDIwNzk2Rjc1MjA2OTczMjA2QzZGNkY3MycsCic2MzY4NjU3MjYzNjg2NTcyNkM2MTMwNjM2MzY2NjU2RDZENjUnLAonNjE2NTY4Njg3MjY1MzA2MzYzNzI2RDY1NjM2RDZDNjY2NTYzJywKJzYzNjg2NTcyNjM2ODY1NzI2QzYxMzA2MzYzNjY2NTZENkQ2NScsCic2MzYxNkM2MTZBNkM2MTYxNjc2MjZBNzI2QjZDNjYzMDYzNjMnLAonQzY2NjU2MzYxNjU2ODY4NzI2NTcyMzA2MzYzNkQ2NTYzNkQ2JywKJzMwNjM2MzYyNkM2MTY2NkM2MTYzNkM2MTcyNkE2MTY3NkE2QicsCic2MzYxNkM2MTZBNkM2MTYxNjc2MjZBNzI2QjZDNjYzMDYzNjMnLAonMzAzMDMwNjY3NTc1NzM3MzZDNjY2QzZCNkU3MzY3MzA2MzYzJywKJzMwMzAzMDY2NzU3NTczNzM2QzY2NkM2QjZFNzM2NzMwNjM2MycsCiczMDYzNjM3NTc1NzM3MzZDNjE2QTZDNjE2MTY3NjI2NkU3NkInLAonNjI3MjY1NjUzMzcyNjU2NTMzMzMzMzMzMzM2NDIwMzA2MzYzJywKJzMwNjM2MzIwMjA3NTY2NjY2OTI3NkQ3NDY5NzI2NTY0MjAyMCcsCic2QzZGNjg2QzZGNjMwNjM2Mzg2QzZGNjg2QzZGNjg2QzZGNjgnLAonNjI3NTMwNjM2Mzc0MjA3OTZGNzUyMDY5NzMyMDZDNkY2RjczJywKJzYzNjg2NTcyNjM2ODY1NzI2QzYxMzA2MzYzNjY2NTZENkQ2NScsCidDNjY2NTYzNjE2NTY4Njg3MjY1NzIzMDYzNjM2RDY1NjM2RDYnLAonMzA2MzYzNjI2QzYxNjY2QzYxNjM2QzYxNzI2QTYxNjc2QTZCJywKJzYzNjE2QzYxNkE2QzYxNjE2NzYyNkE3MjZCNkM2NjMwNjM2MycKXQ=="

    res = base64.b64decode(cipher_text)
    massiv = [i.replace("'", "").replace(",", "") for i in res.decode().split('\n')[1:]]

    for i in massiv:
        try:
            flag = bytes.fromhex(i).decode('utf-8')
            if "/4" in flag:
                print(flag)
        except:
            continue


def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def print_board(sudoku_board):
    for i in range(9):
        for j in range(9):
            print(sudoku_board[i][j], end='')
            if j == 2 or j == 5:
                print('|', end='')
        print()
        if i == 2 or i == 5:
            print('=' * 12)


def parse_data(raw_sudoku):
    board = [[None] * 9 for j in range(9)]
    sudoku_list = raw_sudoku.replace('#', '0').replace('|', '').replace('\n', '').replace('-', '').replace('=', '')
    sudoku_list = [int(num) for num in sudoku_list]

    index = 0
    index_list = []
    for i in range(9):
        for j in range(9):
            if sudoku_list[index] == 0:
                index_list.append((i, j))

            board[i][j] = sudoku_list[index]
            index += 1

    return board, index_list


def get_guessed_number(board, index):
    return board[index[0]][index[1]]


def test():
    a = "517600034289004000346205090602000010038006047000000000090000078703400560000000000"
    board, index_list = parse_data(a)
    print_board(board)
    print(index_list)
    print("Solving")
    solveSudoku(board)


HOST = "51.158.112.242"
PORT = 31337

r = pwn.remote(HOST, PORT)
intro = r.recvuntil("So, let's begin! (from kECZnPrIufo)")
print(intro)
time.sleep(5)
r.sendline('a' * 100)

while 1:
    try:
        info = r.recvuntil("Turn: ")

        turn = r.recvline()
        print(f'Turn: {turn.decode()}')

        r.recvuntil(">>>")
        sudoku = r.recvuntil("<<<").decode()[:-3]
        board, index_list = parse_data(sudoku)
        solveSudoku(board)

        r.recvuntil("Your solution:\n")
        for index in index_list:
            solution = get_guessed_number(board, index)
            r.sendline(f"{index[0] + 1} {index[1] + 1} {solution}".encode())
            print(f"Sending line {index[0] + 1} {index[1] + 1} {solution}")

        r.sendline("DONE")
    except:
        r.interactive()

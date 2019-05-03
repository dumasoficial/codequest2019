import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    cycles=int(sys.stdin.readline().rstrip())
    board=[]
    for _ in range(10):
        board.append([int(x) for x in sys.stdin.readline().rstrip()])
    for _ in range(cycles):
        commands=[]
        for x in range(10):
            for y in range(10):
                n=0
                if y>0 and board[x][y-1]:
                    n+=1
                if y<9 and board[x][y+1]:
                    n+=1
                if x>0 and board[x-1][y]:
                    n+=1
                if x<9 and board[x+1][y]:
                    n+=1
                if y>0 and x>0 and board[x-1][y-1]:
                    n+=1
                if y<9 and x>0 and board[x-1][y+1]:
                    n+=1
                if y>0 and x<9 and board[x+1][y-1]:
                    n+=1
                if x<9 and y<9 and board[x+1][y+1]:
                    n+=1
                if board[x][y]:
                    if n>3 or n<2:
                        commands.append([x, y, 0])
                elif n==3:
                    commands.append([x, y, 1])
        for x in commands:
            board[x[0]][x[1]]=x[2]
    for x in range(10):
        for y in board[x]:
            print(y, end='')
        print('')

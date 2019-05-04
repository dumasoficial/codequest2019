import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    h,w = sys.stdin.readline().rstrip().split(' ')
    h=int(h)
    w=int(w)
    board=[[10 for _ in range(20)] for _ in range(20)]
    for y in range(h-2, h+3):
        if y<0 or y>19:
            continue
        for x in range(w-2, w+3):
            if x<0 or x>19:
                continue
            board[y][x]=25
    for y in range(h-1, h+2):
        if y<0 or y>19:
            continue
        for x in range(w-1, w+2):
            if x<0 or x>19:
                continue
            board[y][x]=50
    board[h][w]=100
    for x in board:
        for y in range(20):
            print(x[y], end='')
            if y<19:
                print(' ', end='')
        print('')
            
        

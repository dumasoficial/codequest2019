import sys

def legal(x,y,grid):
    moves=[1,2,3,4,5,6,7,8,9]
    row=[grid[i,y] for i in range(9) if grid[i,y]>0]
    column=[grid[x,i] for i in range(9) if grid[x,i]>0]
    topleft=((x-x%3),(y-y%3))
    peers=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    sector=[grid[topleft[0]+i[0],topleft[1]+i[1]] for i in peers if grid[topleft[0]+i[0],topleft[1]+i[1]]>0]   
    available=[]
    for i in moves:
        if i not in row and i not in column and i not in sector:
            available.append(i)
    return available

def solve(grid):
    empty=[(i,legal(i[0],i[1],grid)) for i in grid if grid[i]==0]
    if not empty:
        return grid
    square,options=min(empty,key=lambda i:len(i[1]))

    if not options:
        raise Exception('No Options')
    for option in options:
        try:
            copy=grid.copy()
            copy[square]=option
            solution=solve(copy)
        except:
            continue
    if solution:
        return solution
    
def display(grid):
    for y in range(9):
        for x in range(9):
            if grid[x,y]==0:
                print('_',end='')
            else:
                print(grid[x,y],end='')
        print()
        
cases = int(sys.stdin.readline().rstrip())
for _ in range(cases):
    grid={}
    for y in range(9):
        line=sys.stdin.readline().rstrip()
        for x,value in enumerate(line):
            try:
                grid[x,y]=int(value)
            except:
                grid[x,y]=0
    display(solve(grid))

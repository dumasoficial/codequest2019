import sys

def available(grid,square):
    moves=[1,2,3,4,5,6,7,8,9]
    row=[grid[s,square[1]] for s in range(9)]
    column=[grid[square[0],s] for s in range(9)]
    topleft=(square[0]-square[0]%3,square[1]-square[1]%3)
    sector=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    peers=[grid[topleft[0]+s[0],topleft[1]+s[1]] for s in sector]
    available=[]
    for move in moves:
        if move in row or move in column or move in peers:
            continue
        available.append(move)
    return available 
    
def solve(grid):
    empty=[s for s in grid if grid[s]==0]
    if not empty:
        return grid
    empty_with_available=[(available(grid,s),s) for s in empty]
    options,square=min(empty_with_available,key=lambda x:len(x[0]))
    if len(options)==0:
        raise Exception('No options')
    for option in options:
        try:
            copy=grid.copy()
            copy[square]=option
            solution=solve(copy)
        except:
            continue
    if solution:
        return solution
    print('Found no solution')
        
def display(grid):            
    for square in grid.keys():
        if grid[square]==0:
            print('_',end='')
        else:       
            print(grid[square],end='')
        if square[0]==8:
            print()

            
cases = int(sys.stdin.readline().rstrip())
for _ in range(cases):
    grid={}
    for y in range(9):
        row=sys.stdin.readline().rstrip()
        for x,value in enumerate(row):
            try:
                grid[x,y]=int(value)
            except:
                grid[x,y]=0
                
    display(solve(grid))

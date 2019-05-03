import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    rows,columns,bombs=[int(i) for i in sys.stdin.readline().split()]
    b=[]
    for _ in range(bombs):
       r,c=sys.stdin.readline().split()
       b.append((int(r),int(c)))
    for r in range(rows):
        temp=''
        for c in range(columns):
            if (r,c) in b:
                temp+='*'
                continue
            neighbors=[(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]
            bomb_count=sum([i in b for i in neighbors])       
            temp+=str(bomb_count)
        print(temp)
        
    

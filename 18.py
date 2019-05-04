import sys

cases = int(sys.stdin.readline().rstrip())
limit=100
for _ in range(cases):
    a,b=sys.stdin.readline().rstrip().split()
    a,b=float(a),float(b)
    c=(a,b)
    z=c
    n=1
    while True:
        abs_z=((z[0]**2)+(z[1]**2))**0.5
        if abs_z>=limit or n>51:break
        a=(z[0]**2)-(z[1]**2)+c[0]
        b=2*(z[0]*z[1])+c[1]
        z=(a,b)
        n+=1
    out=str(c[0])+"+"+str(c[1])+"i" if c[1]>0 else str(c[0])+str(c[1])+"i"
    if n<=10:
        print(out,"RED")
    if n>10 and n<=20:
        print(out,"ORANGE")
    if n>20 and n<=30:
        print(out,"YELLOW")
    if n>30 and n<=40:
        print(out,"GREEN")
    if n>40 and n<=50:
        print(out,"BLUE")
    if n>50:
        print(out,"BLACK")
        
    
    
    

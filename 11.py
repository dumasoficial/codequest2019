import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    l=int(sys.stdin.readline().rstrip())
    n=0
    while True:
        b=bin(n)[2:]
        if len(b)>l:break
        print(("{:0"+str(l)+"b}").format(n))
        n+=1

import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n1, n2 = sys.stdin.readline().rstrip().split(' ')
    n1=int(n1)
    n2=int(n2)
    if n1==n2:
        print(2*(n1+n2))
    else:
        print(n1+n2)
    

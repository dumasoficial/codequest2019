import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n1, n2, n3 = sys.stdin.readline().rstrip().split(' ')
    n1=int(n1)
    n2=int(n2)*5
    n3=int(n3)
    if (n1+n2)<n3:
        print("false")
    else:
        print("true")

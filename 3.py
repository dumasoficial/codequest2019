import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n1, n2 = sys.stdin.readline().rstrip().split(' ')
    n1 = (n1=="true")
    n2= (n2=="true")
    if (n1 or n2) and  not (n1 and n2):
        print('false')
    else:
        print('true')

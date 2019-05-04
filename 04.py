import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n1, n2 = sys.stdin.readline().rstrip().lower().split(' ')
    n2 = (n2=="true")
    n1=int(n1)
    if n2:
        if n1<66:
            print("no ticket")
        elif 65<n1<86:
            print("small ticket")
        else:
            print("big ticket")
    else:
        if n1<61:
            print("no ticket")
        elif 60<n1<81:
            print("small ticket")
        else:
            print("big ticket")

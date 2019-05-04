import sys, math

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n1 = int(sys.stdin.readline().rstrip())
    n1+=(40075/2/math.pi)
    print(round(2*math.pi*n1, 1))

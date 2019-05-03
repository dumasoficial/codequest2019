import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    data=[]
    for _ in range(int(sys.stdin.readline().rstrip())):
        data.append(float(sys.stdin.readline().rstrip()))
    ma = max(data)
    mi = min(data)
    for x in data:
        print(round((x-mi)/(ma-mi)*255))

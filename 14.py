import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n=int(sys.stdin.readline().rstrip())
    d={}
    for _ in range(n):
        start,destination=sys.stdin.readline().split()
        d[start]=destination

    start=[i for i in d.keys() if not i in d.values()][0]
    path=[start]
    for _ in range(len(d.items())):
        path.append(d[path[-1]])
    for i in path[::-1]: print(i)
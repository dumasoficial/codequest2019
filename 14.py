import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n=int(sys.stdin.readline().rstrip())
    cities=[]
    for _ in range(n):
        i=sys.stdin.readline().split()
        cities.append([i[0],i[1]])
    d=dict((i[0],i[1]) for i in cities)
    starts=[i[0] for i in cities]
    destinations=[i[1] for i in cities]
    start=''.join([i for i in starts if not i in destinations])
    path=[start]
    for _ in range(len(starts)):
        path.append(d[path[-1]])
    for i in path[::-1]: print(i)

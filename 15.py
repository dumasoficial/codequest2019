import sys

cases = int(sys.stdin.readline().rstrip())
alph='abcdefghijklmnopqrstuvwxyz'
numeric_value=lambda word: sum([alph.index(i)+1 for i in word])
for _ in range(cases):
    data=sys.stdin.readline().split()
    times=[int(i) for i in sys.stdin.readline().split()]
    hashes=[0]
    for i,d in enumerate(data):
        h=(times[i]+numeric_value(d)+(i+1)+hashes[i])*50/147
        hashes.append(h)
    print(round(hashes[-1]))

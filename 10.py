import sys

cases = int(sys.stdin.readline().rstrip())
alpha=[chr(x) for x in range(97,123)]

for _ in range(cases):
    shift=int(sys.stdin.readline().rstrip())
    msg=sys.stdin.readline().rstrip().lower()
    final=""
    for x in msg:
        if x==" ":
            final+=x
        else:
            final+=alpha[alpha.index(x)-shift]
    print(final)

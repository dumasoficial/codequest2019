import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n=int(sys.stdin.readline().rstrip())
    ips=[]
    for _ in range(n):
        ip=sys.stdin.readline().rstrip()
        b=''.join(["{:08b}".format(int(x)) for x in ip.split('.')])
        ips.append(b)
    common=0
    same=True
    for di,d in enumerate(ips[0]):
        for i in ips:
            if i[di]!=d:same=False
        if not same:break
        common+=1
    ip=ip.split('.')
    out=ip[:(common//8)]
    remaining=ips[0][(common//8)*8:common]
    if remaining:
        remaining='{:<08}'.format(remaining)
        out.append(str(int(remaining,2)))
    out.extend(['0']*(4-len(out)))
    print('.'.join(out)+"/"+str(common))
    

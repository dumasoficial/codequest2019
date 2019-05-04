import sys, operator

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    n=int(sys.stdin.readline().rstrip())
    encrypted=sys.stdin.readline().rstrip()
    keys=[]
    for _ in range(n):
        keys.append(sys.stdin.readline().rstrip())
    for key in keys:
        out='['
        for c in range(0,len(key)-2,2):
            h=encrypted[c:c+2]
            h2=key[c:c+2]
            xor=int(bin(int(h,16)),2)^int(bin(int(h2,16)),2)
            out+=chr(xor)
        print(out+']')
        

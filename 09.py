import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    i=(sys.stdin.readline().rstrip().lower())
    j=i.replace(',',' ').replace('and',' ').split()
    h,m,s=0,0,0
    for word in j:
        if 'h' in word:
            h=word.split('h')[0]
        if 'm' in word:
            m=word.split('m')[0]
        if 's' in word:
            s=word.split('s')[0]
    print("{0:02}:{1:02}:{2:02}".format(int(h), int(m), int(s)))
    

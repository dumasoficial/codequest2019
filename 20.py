import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    k,u=sys.stdin.readline().split()
    known=[]
    d={}
    for _ in range(int(k)):
        name,length,width,wing,angle=sys.stdin.readline().split()
        length,width,wing,angle=float(length),float(width),float(wing),float(angle)
        d[length,width,wing,angle]=name
    for _ in range(int(u)):
        unknown_data=[float(i) for i in sys.stdin.readline().split()]
        dists={}
        k=5
        for data_point in d.keys():
            dist=sum([(i-j)**2 for i,j in zip(data_point,unknown_data)])**0.5
            dists[dist]=data_point
            sorted_keys=sorted(list(dists.keys()))
        while True:
            k_nearest=sorted_keys[:k]
            a=sum([d[dists[i]]=='Accipitridae' for i in k_nearest])
            p=sum([d[dists[i]]=='Passeridae' for i in k_nearest])
            c=sum([d[dists[i]]=='Cathartidae' for i in k_nearest])
            #print(a,p,c)
            if a>p and a>c:
                print('Accipitridae')
                break
            if p>a and p>c:
                print('Passeridae')
                break
            if c>a and c>p:
                print('Cathartidae')
                break
            k+=1
    

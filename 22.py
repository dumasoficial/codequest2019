
import sys,datetime
cases = int(sys.stdin.readline().rstrip())
today=datetime.datetime(2019,4,27)#Code Quest 2019 date.datetime.datetime.today()
for _ in range(cases):
    number_files,size_drive=sys.stdin.readline().rstrip().split(' ')
    number_files,size_drive=int(number_files),float(size_drive)
    files=[]
    for file in range(number_files):
        date,time,ampm,size,name=(sys.stdin.readline().rstrip().split(' '))
        day,month,year=[int(i) for i in date.split('/')]
        size=float(size)/1000 #MB
        age=(today-datetime.datetime(year,month,day)).days
        if 'PM' in ampm:age-=0.5
        #print(age,age*int(size))
        files.append([name,age*size,size])
              
    files.sort(key=lambda x:x[1])
    total=0
    while total<size_drive*1000*0.25:
        name,score,size=files.pop()
        total+=size
        print(name,"{:.3f}".format(score))
    
        
    
    
    

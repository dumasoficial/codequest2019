import sys

cases = int(sys.stdin.readline().rstrip())
for _ in range(cases):
    seen=False
    xs,ys,xc,yc,w=(sys.stdin.readline().rstrip().split(' '))
    xs,ys,xc,yc,w=float(xs),float(ys),float(xc),float(yc),int(w)
    try:
        slope_camera=(yc-ys)/(xc-xs)        
    except:
        slope_camera=0.0
    cs=ys-slope_camera*xs   
    for wall in range(w):
        xw,yw,xw2,yw2=sys.stdin.readline().rstrip().split(' ')
        xw,yw,xw2,yw2=float(xw),float(yw),float(xw2),float(yw2)
        try:
            slope_wall=(yw2-yw)/(xw2-xw)
        except:
            slope_wall=0.0
        cw=yw-slope_wall*xw
        int_x=(cw-cs)/(slope_camera-slope_wall)
        int_y=(slope_camera*int_x)+cs
        if int_x<=10.0 and int_x>=0.0 and int_y<=10.0 and int_y>=0:
            seen=True
    if seen:print('No')
    if not seen:print('Yes')
        
    

    

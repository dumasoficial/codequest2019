#An adapted A* algorithm
import sys

class Node(object):
    def __init__(self,parent=None,position=None):
        self.parent=parent
        self.position=position
        self.g=0
        self.h=0
        self.f=0
    def __eq__(self,other):
        return self.position==other.position
 
cases = int(sys.stdin.readline().rstrip())
  
for _ in range(cases):
    w, h=[int(i) for i in sys.stdin.readline().split()]
    building=[]
    exits=[]
    d={}
    for i in range(h):
        line=sys.stdin.readline().rstrip().ljust(w)
        building.append(line)
        for j,value in enumerate(line):
            if value=='o':
                initial=Node(None,(i,j))
            if value=='X':
                exits.append((i,j))
            d[i,j]=value
    
    #print(initial.position,exits)
    path=[]
    initial.g=initial.h=initial.f=0
    open_list=[initial]
    closed_list=[]

    while open_list:
        current_node=open_list[0]
        current_index=0
        for index,item in enumerate(open_list):
            if item.f<current_node.f:
                current_node=item
                current_index=index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if d[current_node.position]=='X':
            path=[]
            current=current_node
            while current is not None:
                path.append(current.position)
                current=current.parent
            break
        
        possible=[(current_node.position[0]+i[0],current_node.position[1]+i[1]) for i in [(-1,0),(0,-1),(1,0),(0,1)]]
        children=[Node(current_node,child) for child in possible if d.get(child)==' ' or d.get(child)=='X']
        #print(current_node.position,[i.position for i in children],possible)
        for child in children:
            if child in closed_list:continue
            child.g=current_node.g+1
            child.h=min([((child.position[0]-end[0])**2)+(child.position[1]-end[1])**2 for end in exits])
            child.f=child.g+child.h
            for open_node in open_list:
                if child==open_node and child.g>open_node.g:
                    continue
            open_list.append(child)
            
    if not path:
        print('No path. Check input. ')
        continue

    for i,row in enumerate(building):
        for j,column in enumerate(row):
            if (i,j) in path and (i,j)!=initial.position and (i,j) not in exits:
                print('.',end='')
            else:
                print(d[(i,j)],end='')
        print('')


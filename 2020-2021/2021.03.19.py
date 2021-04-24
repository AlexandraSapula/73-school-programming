print("ok")
x1=5
y1=3
x2=-5
y2=10

dir=""
x=x1
y=y1
while x!=x2 or y!=y2 :
    if y<y2 :
        y=y+1
        dir += 'N'
    elif y>y2 :
        y=y-1
        dir += 'S'
        
    if x<x2 :
        x=x+1
        dir += 'W'
    elif x>x2 :
        x=x-1
        dir += 'E'

    dir += " "
    
print(dir)
        


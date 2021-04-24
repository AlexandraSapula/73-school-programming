import random

def min(m) :
    r=m[0]
    for v in m :
        if v < r :
            r = v
    return r

def sum(m) :
    r=0
    for v in m :
        r=r+v
    return r
        
def mid(m) :
    return sum(m)/len(m)

print("Ok")
a=[]
n=10
while n>0 :
    a.append(random.randint(1,5))
    n-=1
    
for k in a :
    print(k)
    
print("-- min --")
print(min(a))
print("-- mid --")
print(mid(a))



import random

def nearest(m,v) :
    k=m[0]
    kp=abs(k-v)
    for a in m :
        d=abs(a-v)
        if d<kp :
            k=a
            kp=d
            if kp==0 :
                return k
    return k

a=int(input("enter namber : "))
print(a)
#print("enter number")
w=[]
n=10
while n>0 :
    w.append(random.randint(0,1000))
    n-=1
print(w)
f=nearest(w, a)
#print(nearest(w,a))
#nearest(13) = 17(4)
print("nearest({0}) = {1}({2}) ".format(a, f, f-a))




    

    
    
    
    

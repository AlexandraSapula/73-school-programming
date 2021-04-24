def mults(n) :
    d=2
    r=[]
    while n>1 : 
        k = n % d
        if k==0 :
            r.append(d)
            n=n//d
        else :
            d=d+1
    return r
            
        
    
a=int(input("enter namber : "))
print(a)
print(mults(a))

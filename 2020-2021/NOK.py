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

a=[]
while True :
    s=input("n = ")
    if not s :
        break
    m=int(s)
    a.append(m)

print(a)
for w in a :
    print(mults(w))


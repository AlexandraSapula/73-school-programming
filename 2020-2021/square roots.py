import math

while True :

    print("input a,b,c of quadratik")
    str_a=input("a = ")
    if not str_a :
        break
        
    a=float(str_a)

    if a==0.0 :
        print("non-quadratic")
        continue
        
    b=float(input("b = "))
    c=float(input("c = "))
    print(  "{0}x^2 {1:+}x {2:+} = 0".format(a,b,c)  )

    

    if c==0.0 and b==0 :
        print ("x1=x2=0")
    
    elif c==0.0 :
        print("x1=0")
        print("x2={0}/{1}={2}".format(-b,a,-b/a))

    elif b==0.0 :
        print("x=+-sqrt({0}/{1})".format(-c,a))
        x=math.sqrt(-c/a)
        print("x1=",-x)
        print("x2=",x)

    elif a+c==b :
        print("x1=-1")
        print("x2={0}/{1}={2}".format(-c,a,(-c)/a))

    elif a+c==-b :
        print("x1=1")
        print("x2={0}/{1}={2}".format(c,a,(c)/a))
    
    else :
        #desk
        D=b**2-4*a*c
        print("D =",D)
        if D<0.0 :
            print("no roots")
        
        elif D==0.0 :
            print("x1=x2={0}/2*{1}={2}".format(-b,a,-b/(2*a)))
        
        else :
            print("x={0}+-sqrt({1})/2*{2}".format(-b,D,a))
            # x1=(-b-sqrt(D))/(2*a)
            print("x1=",(-b-math.sqrt(D))/(2*a))
            # x2=(-b+sqrt(D))/(2*a)
            print("x2=",(-b+math.sqrt(D))/(2*a))

print("Good Bye")
quit()

from math import*
print("input a,b,c of quadratik")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
print("a*x**2+b*x+c=0")
D=b**2-4*a*c
print("D =",D)
if D<0.0 :
    print("no roots")
        
elif D==0.0 :
    print("x1=x2=(-b)/(2*a)")
    print("x1=x2=",(-b)/(2*a))
        
else :
    print(x=(-b)+-sqrt(D)/(2*a))
    # x1=(-b-sqrt(D))/(2*a)
    print("x1=",(-b-math.sqrt(D))/(2*a))
    # x2=(-b+sqrt(D))/(2*a)
    print("x2=",(-b+math.sqrt(D))/(2*a))
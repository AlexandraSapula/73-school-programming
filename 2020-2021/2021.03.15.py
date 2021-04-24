from math import*
print("input a,b,c of quadratik")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
print(  "{0}x^2 {1:+}x {2:+} = 0".format(a,b,c)  )
D=b**2-4*a*c
print("D =",D)
if D<0.0 :
    print("no roots")
    
elif D==0.0 :
    print("x1=x2={0}/2*{1}={2}".format(-b,a,-b/(2*a)))
        
else :
    print("x={0}+-sqrt({1})/2*{2}".format(-b,D,a))
    # x1=(-b-sqrt(D))/(2*a)
    print("x1=",((-b)-sqrt(D))/(2*a))
    # x2=(-b+sqrt(D))/(2*a)
    print("x2=",((-b)+sqrt(D))/(2*a))
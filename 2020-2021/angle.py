import math

def veclen(x,y) :
    return math.sqrt(x**2+y**2)

print("Hello")

str_x1=input("x1 = ")
if not str_x1 :
    quit()

x1=float(str_x1)
y1=float(input("y1 = "))
x2=float(input("x2 = "))
y2=float(input("y2 = "))

prod=x1*x2+y1*y2

len1=veclen(x1,y1)
len2=veclen(x2,y2)
cos_a=prod/(len1*len2)
print("cos(a)=",cos_a)

print("prod = ",prod)
cross_prod=x1*y2-x2*y1
print("cross_prod",cross_prod)

if cross_prod==0 :
    if prod>0 :
        print ("0")
    if prod<0 :
        print ("180")

elif prod==0 :
    print ("90")

elif prod>0 :
    print ("acute angle")

elif prod<0 :
    print("obtuse angle")

print("Good Bye")
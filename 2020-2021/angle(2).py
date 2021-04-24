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

if cos_a==1 :
    print("0")
elif cos_a==0 :
    print("90")
elif cos_a==-1 :
    print("180")
elif cos_a>0 :
    print ("Острый")
else :
    print("Тупой")
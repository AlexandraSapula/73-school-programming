print("Hello")
x=float(input("x="))
y=float(input("y="))
if x>0.0 and y>0.0 :
    print("First")
elif x<0.0 and y>0.0 :
    print("Second")
elif x<0.0 and y<0 :
    print("Third")
else :
    print("Fourth")
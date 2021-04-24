print("Hello")
while True :
    
    str_x=input("x = ")
    if not str_x :
        break

    x=float(str_x)
    y=float(input("y = "))

    if x==0.0 and y==0.0 :
        print("Origin")

    elif x==0.0 :
        print ("In oy")

    elif y==0.0 :
        print ("In ox")

    elif x>0.0 :
        if y<0.0 :
            print("Fourth")
        else :
            print("First")

    else :
        if y<0.0 :
            print("Third")
        else :
            print("Second")
            
    quit()
    
print("Good Bye!")

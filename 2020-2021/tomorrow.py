print("Hello")
str_n=input("n = ")
if not str_n :
    quit()

n=int(str_n)
m=int(input("m = "))
y=int(input("y = "))
year= y % 4==0 and y %100!=0 
mon=m==1  or m==3 or m==5 or m==7 or m==8 or m==10
mon_1=m==4 or m==6 or m==9 or m==11

if m>12 :
    print("Good Bye")
    quit()

if mon :
    if n>31 :
        print("Good Bye")
        quit()

elif mon_1 :
    if n>30 :
        print("Good Bye")
        quit()

elif m==12 :
    if n>31 :
        print("Good Bye")
        quit()
elif m==2 :
    if year :
        if n>29 :
            print("Good Bye")
            quit()
    else :
        if n>28 :
            print ("Good Bye")
            quit()

print (n,".",m,".",y)

if mon  :
    if n==31 :
        print(1,".",m+1,".",y)
    elif n<31 :
        print (n+1,".",m,".",y)

elif mon_1 :
    if n==30 :
        print(1,".",m+1,".",y)
    elif n<30 :
        print(n+1,".",m,".",y)

elif m==12 :
    if n==31 :
        print(1,".",1,".",y+1)
    elif n<31 :
        print (n+1,".",m,".",y)

else :
    if year :
        if n==29 :
            print(1,".",m+1,".",y)
        elif n<29 :
            print (n+1,".",m,".",y)
    else :
        if n<28 :
            print (n+1,".",m,".",y)
        if n==28 :
            print(1,".",m+1,".",y)
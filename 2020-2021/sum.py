c=0
for a in range(100,201,1) :
    if a % 6 ==0 :
        c+=a
    else :
        continue
print("S = ",c)
a=[]
while True :
    s=input("n = ")
    if not s :
        break
    m=int(s)
    a.append(m)

result=""

for n in a :
    if result :
        result = result + ", "

    result = result + str(n)
    
result = "{" + result + "}"
print(result) 
        
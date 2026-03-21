s=input("enter the string : ")
imp=[]
count=0
for i in s:
    if i in imp:
        continue
    elif i!=" " :
        for j in s:
            if i==j:
                count+=1
        imp.append(i)
        print(f"{i} occours {count} times")
        count=0
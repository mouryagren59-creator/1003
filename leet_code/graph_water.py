height=[0,1,0,2,1,0,1,3,2,1,2,1]
big=0
iindex=0
jindex=0
for i in height:
    for j in height[iindex+1::]:
        jindex+=1
        if i>j :
            if j*jindex>big:
                big=j*jindex
            else :
                if i*jindex>big:
                    big=i*jindex
    iindex+=1
    jindex=0
print(big)
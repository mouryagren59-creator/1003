def sum(wh,target):
    final=[]
    for i in range(len(wh)-1):
        for j in range(i,len(wh)):
            if wh[i]+wh[j]==target:
                final.append([i,j])
    return final

wh=[1,2,3,4,5]
target=7
final=sum(wh,target)
print(final)
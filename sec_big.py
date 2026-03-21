l=[111,5,3,4,56,4,5,6,4,3,76,6,3,45]
big=max(l)
if l.index(big)==0:
    big2=l[1]
else:
    big2=l[0]
for i in l:
    if i>big2 and i<big:
        big2=i
print(big2)
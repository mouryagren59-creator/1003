a=[]
b=[]
c=[]
size=int(input("enter the no of elements : "))
for i in range(size):
    new=int(input("enter the data : "))
    a.append(new)
while(len(a)>0):
    small=min(a)
    a.remove(small)
    b.append(small)
    c.append(max(b)-min(b))
    print(c)
print(sum(c))


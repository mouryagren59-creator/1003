def kMax(l,k):
    i=1
    while(i!=k):
        big=max(l)
        l.remove(big)
        i+=1
    return max(l)

print(kMax([10,2,4,5,7,9],2))
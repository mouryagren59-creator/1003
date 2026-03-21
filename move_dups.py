def movedups(string):
    d1={}
    p=""
    q=""
    for i in string:
        if i not in d1.keys():
            d1[i]=1
            p=p+i
        else :
            q=q+i
    print(f"{p}_{q}")
movedups("aaabbbcdff")
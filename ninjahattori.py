def shift(s,acount=0,ccount=0):
    final=s
    len_str=len(s)
    if(ccount>0):
        final=s[len_str-ccount::]+s[:len_str-ccount:]
    if(acount>0):
        final=final[acount::]+final[:acount:]
    return final
    
acount=int(input("enter the acount : "))
ccount=int(input("enter the ccount : "))
print(shift("NinjaHattori",acount=acount,ccount=ccount))
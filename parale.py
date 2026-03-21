size=int(input("enter the parallalogram : "))
for i in range(0,size):
    for s in range(0,i):
        print("  ",end="")
    if i==0 or i==size-1:
        for l in range(0,size):
            print("*     ",end="")
    else :
        for l in range(0,size):
            if l==0 or l==size-1:
                print("*     ",end="")
            else :
                print("      ",end="")
    print("\n")
# side=int(input("enter the size of triangle : "))
# for i in range(1,side+1):
#     if(i==1 or i==side):
#         for j in range(0,i):
#             print("* ",end="")
#     else :
#         for k in range(1,i+1):
#             if(k==1 or k==i):
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#     print("\n")

side=int(input("enter the size of triangle : "))
for i in range(1,side+1):
    for j in range(side-i,0):
        print("  ",end="")
    for k in range(i):
        print("* ",end="")
    print("\n")
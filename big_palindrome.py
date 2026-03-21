word=input("enter the string : ")
index1=0
biglen=0
bigpal=""
# words=[]
for i in word:
    index2=len(word)
    for j in word[::-1]:
        if i==j:
            s=word[index1:index2]
            if s==s[::-1]:
                # words.append(s)
                if(len(s)>=len(bigpal)):
                    bigpal=""+s
                break
        index2-=1
    index1+=1
print(bigpal)
# print(words)
# leng=[]
# i=0
# for j in words:
#     leng.append(len(j))
# i=leng.index(max(leng))
# print("biggest palindrome is",words[i])
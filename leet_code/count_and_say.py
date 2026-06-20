#this is one of the toughest problem I've ever faced damn
class Solution(object):
    count=1
    def countAndSay(self,n):
        count=1
        def cas(fin,count):
            st=str(fin)
            fina=""
            i=0
            while i<len(st):
                ct=1
                while i+1<len(st) and st[i]==st[i+1]:
                    ct+=1
                    i+=1
                fina+=str(ct)+st[i]
                i+=1
            if count+1==n:
                return fina
            else:
                return cas(fina,count+1)
        if n==1:
            return "1"
        else:
            return cas("1",count)
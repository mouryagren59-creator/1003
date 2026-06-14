class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)>0 and strs[0]!="":
            one=strs[0][0]
        else :
            return ""
        flag=1
        output=""
        index=0
        while(flag==1):
            for i in strs:
                if len(i)-1>=index:
                    if one!=i[index]:
                        flag=0
                        break
                else :
                    flag=0
                    break
            if flag==1:
                output=output+i[index]
            index+=1
            if len(strs[0])-1>=index:
                one=strs[0][index]
            else :
                break
        return output    
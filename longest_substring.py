class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s==" ":
            return 1
        st=s
        large=""
        le=0
        start=0
        while start<len(s):
            temp=0
            i=start
            lis=""
            while i<len(s) and s[i] not in lis:
                lis+=s[i]
                i+=1
                temp+=1
            if temp>le:
                le=temp
            start+=1
        return le
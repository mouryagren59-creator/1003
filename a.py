class Solution(object):
    def removeDuplicates(self, nums):
        check={}
        final=[]
        dups=0
        for i in nums:
            if i not in check.keys():
                nums[i]=1
                final.append(int(i))
            else :
                dups+=1
        for i in range(dups):
            final.append(_)
        return final
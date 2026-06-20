class Solution(object):
    def removeDuplicates(self, nums):
        final=[]
        count=0
        for i in nums:
            if i not in final:
                final.append(int(i))
                nums[count]=int(i)
                count+=1
        return len(final)
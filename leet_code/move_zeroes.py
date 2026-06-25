class Solution(object):
    def moveZeroes(self, nums):
        fin=[]
        count=0
        id=0
        for i in nums:
            if i!=0:
                nums[id]=i
                id+=1
            else:
                count+=1
        for i in range(count):
            nums[id]=0
            id+=1
        nums
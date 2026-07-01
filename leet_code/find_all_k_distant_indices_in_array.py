class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        loc=[]
        fin=[]
        for i in range(len(nums)):
            if nums[i]==key:
                loc.append(i)
        if not loc:
            return loc
        for i in range(len(nums)):
            for j in loc:
                if abs(i-j)<=k:
                    fin.append(i)
                    break
        return fin
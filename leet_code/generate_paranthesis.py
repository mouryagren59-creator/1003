class Solution(object):

    def generateParenthesis(self, n):
        def isValid(s):
            stack = []
            pairs = {
                ')': '(',
                '}': '{',
                ']': '['
            }

            for ch in s:
                if ch in pairs.values():
                    stack.append(ch)
                else:
                    if not stack or stack[-1] != pairs[ch]:
                        return False
                    stack.pop()

            return len(stack) == 0
        ans=[]
        def par(final):
            if len(final)!=2*n:
                final1=final+"("
                final2=final+")"
                par(final1)
                par(final2)
            if len(final)==2*n:
                ans.append(final)
        

        final=""
        final=par(final)
        s=0
        k=0
        fa=[]
        for i in ans:
            st=i
            for j in st:
                if j=="(":
                    s+=1
                elif j==")":
                    k+=1
            if s==k:
                if isValid(st):
                    fa.append(st)
            s=0
            k=0
        return fa
        """
        :type n: int
        :rtype: List[str]
        """
        
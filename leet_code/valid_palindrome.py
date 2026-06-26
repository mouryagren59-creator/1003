class Solution(object):
    def isPalindrome(self, s):
        k=""
        s=s.lower()
        for i in s:
            if i.isalpha():
                k+=i
            if i.isdigit():
                k+=i
        if k==k[::-1]:
            return True
        else :
            return False
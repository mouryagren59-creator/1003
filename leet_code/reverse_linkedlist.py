class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        temp = head
        temp1 = temp.next
        head.next = None

        while temp1 is not None:
            temp2 = temp1.next
            temp1.next = temp
            temp = temp1
            temp1 = temp2

        return temp
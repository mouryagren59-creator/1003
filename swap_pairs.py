class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return head
        elif head.next == None:
            return head

        temp = head
        ret = head.next
        prev = None

        while temp != None and temp.next != None:
            k = temp.next
            chad = k.next

            k.next = temp
            temp.next = chad

            if prev != None:
                prev.next = k

            prev = temp
            temp = chad

        return ret
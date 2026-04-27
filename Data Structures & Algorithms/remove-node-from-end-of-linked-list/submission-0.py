# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy 
        #r = head + n
        r = head
        #getting to r to right position 
        while n > 0 and r:
            r = r.next
            n -= 1
        #getting l to correct position 
        while r:
            l = l.next
            r = r.next
        #delete
        l.next = l.next.next
        return dummy.next
        
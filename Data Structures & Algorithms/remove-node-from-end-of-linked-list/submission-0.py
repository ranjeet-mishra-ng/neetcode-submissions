# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        for i in range(n):
            if not curr:
                return head
            curr = curr.next
        
        if curr == None:
            return head.next
        
        first = head
        second = curr

        while second.next:
            second = second.next
            first = first.next
        
        # first refers to node before the one to be deleted
        temp = first.next
        first.next = first.next.next
        del temp

        return head

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        if not head:
            return None
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Heades of first and reverse of second half
        head2 = prev
        head1 = head

        while head2:
            t1, t2 = head1.next, head2.next
            head1.next = head2
            head2 = t2
            head1.next.next = t1
            head1 = t1
    
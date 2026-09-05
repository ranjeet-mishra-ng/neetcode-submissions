# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode()
        curr = temp_head

        head1 = list1
        head2 = list2

        while head1 and head2:

            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        

        if head1:
            curr.next = head1
        else:
            curr.next = head2
        
        return temp_head.next
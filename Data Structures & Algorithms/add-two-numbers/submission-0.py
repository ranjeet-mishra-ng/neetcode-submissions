# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        resnode = None
        carry = 0
        sum = 0
        head = None

        while h1 or h2:
            if h1:
                sum += h1.val
                h1 = h1.next
            
            if h2:
                sum += h2.val
                h2 = h2.next
            
            sum += carry

            node = ListNode(sum%10)
            carry = sum // 10
            sum = 0

            if resnode == None:
                head = resnode = node
            else:
                resnode.next = node
                resnode = resnode.next
        if carry:
            resnode.next = ListNode(carry)
        return head
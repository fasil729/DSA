# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, curr = dummy, head

        while curr:
            if n <= 0:
               prev = prev.next

            curr = curr.next
            n -= 1
        
        prev.next = prev.next.next

        return dummy.next

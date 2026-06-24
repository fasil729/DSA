# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None, None)
        curr = dummy
        
        k = len(lists)
        
        while curr:
            min_idx = -1
            for idx in range(k):
                node = lists[idx]
                if not node:
                    continue

                if min_idx == -1 or node.val < lists[min_idx].val:
                    min_idx = idx

            
            if min_idx == -1:
                break
            
            min_node = lists[min_idx]
            lists[min_idx] = min_node.next
            min_node.next = None
            curr.next = min_node
            curr = curr.next


        return dummy.next 




        
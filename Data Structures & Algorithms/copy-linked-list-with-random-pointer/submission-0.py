"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_map = {}
        dummy = Node(0)
        copy = dummy
        curr = head

        while curr:
            copy.next = Node(curr.val)
            copy.next.random = curr.random
            nodes_map[curr] = copy.next
            copy = copy.next
            curr = curr.next

        
        copy = dummy.next
        while copy:
            if copy.random:
                copy.random = nodes_map[copy.random]
            copy = copy.next
        

        return dummy.next

        
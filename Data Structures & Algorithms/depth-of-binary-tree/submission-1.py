# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            new_q = deque()
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            level += 1
        return level



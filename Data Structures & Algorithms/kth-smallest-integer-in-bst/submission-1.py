# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, ans = self.helper(root, 0, k) 
        return ans

    def helper(self, root, before, k):
        if not root:
            return 0, None
        
        left_nodes, ans = self.helper(root.left, before, k)
        curr = left_nodes + before + 1 
        if ans:
            return curr, ans
        elif curr == k:
            return curr, root.val
        
        right_nodes, ans = self.helper(root.right, curr, k)
        return left_nodes + right_nodes + 1, ans
        
        
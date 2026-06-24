# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0


            left = dfs(root.left)

            res = max(res, left + root.val)

            right = dfs(root.right)

            res = max(res, right + root.val + left)
            res = max(res, right + root.val)

            return max(0, left + root.val, right + root.val)
        

        dfs(root)
        
        return res
                
        
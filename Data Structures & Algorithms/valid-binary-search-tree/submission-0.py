# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        infinity = float("infinity")
        negative_infinity = float("-infinity")
        return self.helper(root, infinity, negative_infinity)

    def helper(self, root, maxi, mini):
        if not root:
            return True
        if not mini < root.val < maxi:
            return False
        return self.helper(root.left, root.val, mini) and self.helper(root.right, maxi, root.val)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = {val:i for i, val in enumerate(preorder)}
        in_index = {val:i for i, val in enumerate(inorder)}
        leng = len(preorder)


        def dfs(pre_l, pre_r, in_l):
            if pre_l > pre_r:
                return None
            
            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            ind = in_index[root_val]
            mid = ind - in_l

            left = dfs(pre_l + 1, pre_l + mid, in_l)
            right = dfs(pre_l + mid + 1, pre_r, ind + 1)

            root.left = left
            root.right = right

            return root

        
        return dfs(0, leng - 1, 0)
        
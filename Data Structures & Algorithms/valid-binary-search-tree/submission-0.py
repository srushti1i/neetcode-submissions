# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(low, high, root):
            if not root:
                return True
            if low<root.val<high:
                return (
                    dfs(low,root.val, root.left) and
                    dfs(root.val, high, root.right)
                )
            else:
                return False
        low=float('-inf')
        high=float('inf')
        return dfs(low,high,root)

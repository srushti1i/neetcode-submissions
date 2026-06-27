# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=0
        ans=None
        def dfs(root):
            nonlocal cnt,ans
            if not root or ans is not None:
                return 
            dfs(root.left)
            cnt+=1
            if cnt==k:
                ans=root.val
                return 
            dfs(root.right)       
        dfs(root)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dictin={value:i for i, value in enumerate(inorder)}
        pre=0
        def Build(in_l, in_r):
            nonlocal pre
            if in_l>in_r:
                return None
            root=TreeNode(preorder[pre])
            pos=dictin[preorder[pre]]
            pre+=1
            root.left=Build(in_l, pos-1 )
            root.right=Build(pos+1, in_r )
            return root
        return Build(0,len(preorder)-1)
        
        
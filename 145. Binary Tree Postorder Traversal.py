# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recursion(root):
            if root :                
                recursion(root.left)
                recursion(root.right)
                ans.append(root.val)
            else:
                return
        recursion(root)
        return ans
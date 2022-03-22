# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # print (root)
        ans = []
        def recursion(root):
            if root :
                ans.append(root.val)
                recursion(root.left)
                recursion(root.right)
            else:
                return
        recursion(root)
        return ans
        
        
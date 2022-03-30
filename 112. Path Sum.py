# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        def dfs(root,sum):
            if root == None:
                return
            sum += root.val
            if targetSum == sum and root.left == None and root.right == None:
                self.ans = True
            dfs(root.left,sum)
            dfs(root.right,sum)
            return self.ans
        return dfs(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans = False
        self.set = set()
        def dfs(root):
            if root == None:
                return
            if k-root.val in self.set:                
                self.ans = True
            else:
                self.set.add(root.val)                            
                dfs(root.left)                          
                dfs(root.right)
            return self.ans        
        return dfs(root)
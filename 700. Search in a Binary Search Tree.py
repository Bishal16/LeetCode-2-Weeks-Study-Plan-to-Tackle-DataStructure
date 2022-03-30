# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None
        def dfs(root):            
            if root == None:
                return 
            
            if root.val == val:
                # print('ss')
                self.ans = root
                # print(self.ans,root)
                
            
            if val < root.val:
                # print(root.val)
                dfs(root.left)
            if val > root.val:
                dfs(root.right)
            
            return self.ans
        
        return dfs(root)
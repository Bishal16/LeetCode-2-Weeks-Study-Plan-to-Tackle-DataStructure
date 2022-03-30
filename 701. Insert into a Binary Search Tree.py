# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            temp = TreeNode()
            temp.val= val
            return temp
        if val > root.val:
            if root.right == None:
                temp = TreeNode()
                temp.val = val       
                root.right = temp
            else:            
                self.insertIntoBST(root.right, val)
        if val < root.val:
            if root.left == None:
                temp = TreeNode()
                temp.val = val
                root.left = temp
            else:
                self.insertIntoBST(root.left, val)
        return root
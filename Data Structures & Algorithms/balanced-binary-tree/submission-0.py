# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def getheight(root):
            nonlocal balanced
            if not root: 
                return 0
            if not root.left and not root.right:
                return 1
            lefth = getheight(root.left)
            righth = getheight(root.right)
            if abs(lefth-righth) > 1:
                balanced = False
            return 1+max(lefth,righth)
        getheight(root)
        return balanced
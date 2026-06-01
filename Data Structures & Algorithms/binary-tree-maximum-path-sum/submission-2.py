# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        def maxwithnode(node):
            nonlocal maxsum
            if not node:
                return 0
            leftpath = maxwithnode(node.left)
            rightpath = maxwithnode(node.right)
            total = node.val + max(leftpath + rightpath, leftpath, rightpath, 0)
            if total > maxsum:
                maxsum = total
            return node.val + max(leftpath,rightpath,0)
        
        maxwithnode(root)
        return maxsum
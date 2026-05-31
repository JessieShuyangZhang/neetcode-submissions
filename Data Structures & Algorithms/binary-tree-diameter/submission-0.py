# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: 
                return 0;
            if (not root.left and not root.right):
                return 1;
            leftd = dfs(root.left) 
            rightd = dfs(root.right)
            res = max(res, leftd+rightd)
            return 1 + max(leftd, rightd)

        dfs(root)
        return res
        
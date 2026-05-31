# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxseen):
            nonlocal res
            if not node: 
                return None
            if node.val >= maxseen:
                maxseen = node.val
                res += 1
                        
            dfs(node.left, maxseen)
            dfs(node.right,maxseen)
        dfs(root, root.val)
        return res
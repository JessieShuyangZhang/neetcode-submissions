# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = 0

        def dfs(node, maxSeen):
            nonlocal goodnodes
            if not node: 
                return
            
            if maxSeen <= node.val:
                goodnodes += 1
            newmax = max(maxSeen, node.val)
            dfs(node.left, newmax)
            dfs(node.right, newmax)

        dfs(root, root.val)
        return goodnodes

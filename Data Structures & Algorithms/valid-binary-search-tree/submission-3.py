# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        mp = {} # node -> (min, max) of all its sub nodes including itself

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                n = stack.pop()
                if not ((not n.left or mp[n.left][1] < n.val) and (not n.right or mp[n.right][0] > n.val)):
                    return False
                n_min = mp[n.left][0] if n.left else n.val
                n_max = mp[n.right][1] if n.right else n.val
                mp[n] = (n_min, n_max)
        return True

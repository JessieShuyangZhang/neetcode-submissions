# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i, arr = 0, []
        def inorder(node,arr):
            if not node:
                return None
            
            r = inorder(node.left,arr)
            if r == -1:
                return -1
            arr.append(node.val)
            if len(arr) == k:
                return -1
            r = inorder(node.right,arr)
            if r == -1:
                return -1
        inorder(root,arr)
        return arr[-1]
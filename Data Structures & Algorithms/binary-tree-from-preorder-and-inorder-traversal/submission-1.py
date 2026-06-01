# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        cur = head
        i, j, n = 0,0,len(preorder)
        while i<n and j<n: 
            # go right once, then go left as much as possible
            cur.right = TreeNode(val=preorder[i], right=cur.right) # thread to parent
            cur = cur.right
            i += 1
            while j < n and cur.val != inorder[j]:
                cur.left = TreeNode(val=preorder[i], right=cur)
                cur = cur.left
                i += 1
            j += 1
            while j < n and cur.right and cur.right.val == inorder[j]:
                prev = cur.right
                cur.right = None
                cur = prev
                j += 1
        return head.right
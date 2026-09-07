# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_ind = {
            val: ind for ind,val in enumerate(inorder)
        }
        preorder_ind = 0

        def dfs(l, r):
            nonlocal preorder_ind
            if l>r:
                return None

            rootval = preorder[preorder_ind]
            split_ind = inorder_ind[rootval]
            preorder_ind += 1
            root = TreeNode(rootval)
            root.left = dfs(l,split_ind-1)
            root.right = dfs(split_ind+1,r)
            return root
        return dfs(0,len(inorder)-1)
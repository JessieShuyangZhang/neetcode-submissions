# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ppath = self.findPath(root,p)
        qpath = self.findPath(root,q)
        diverged = False
        for i in range(min(len(ppath),len(qpath))):
            if ppath[i].val != qpath[i].val: 
                diverged = True
                break
        return ppath[i-1] if diverged else ppath[i]

    def findPath(self,root: TreeNode, target: TreeNode) -> List[TreeNode]:
        ptr = root
        res = []
        while ptr:
            res.append(ptr)
            if ptr.val < target.val: 
                ptr = ptr.right
            elif ptr.val > target.val:
                ptr = ptr.left
            else:
                return res
            
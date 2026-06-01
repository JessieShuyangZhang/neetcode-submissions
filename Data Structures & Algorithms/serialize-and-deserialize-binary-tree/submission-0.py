# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = ""
        def dfs(node):
            nonlocal preorder
            if not node:
                preorder += "N" if len(preorder)==0 else ",N"
                return
            preorder += str(node.val) if len(preorder)==0 else (","+str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return preorder

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder = data.split(',') # [1,N,2,4,3] [1,2,3,N,N,4,5]
        self.i = 0
        def dfs():
            if inorder[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(inorder[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

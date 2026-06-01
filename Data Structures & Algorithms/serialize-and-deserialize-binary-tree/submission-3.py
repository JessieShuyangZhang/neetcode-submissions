# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q, bfs = deque([root]), []
        while q:
            node = q.popleft()
            if node: 
                bfs.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            if not node:
                bfs.append("N")
        return ','.join(bfs)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        bfs = data.split(",")
        if len(bfs) == 0:
            return None
        root = TreeNode(bfs[0])
        q = deque([root])
        i, n = 0, len(bfs)
        while q and i < n:
            node = q.popleft()
            i += 1
            if i<n and bfs[i] != 'N':
                node.left = TreeNode(int(bfs[i]))
                q.append(node.left)
            i += 1
            if i<n and bfs[i] != 'N':
                node.right = TreeNode(int(bfs[i]))
                q.append(node.right)
        return root

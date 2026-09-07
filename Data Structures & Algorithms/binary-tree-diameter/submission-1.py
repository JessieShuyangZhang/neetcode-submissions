# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        visited = {None: (0,0)} # node -> (height, dia)
        res = 0

        while stack:
            node = stack[-1]
            if node.left and node.left not in visited:
                stack.append(node.left)
            elif node.right and node.right not in visited:
                stack.append(node.right)
            else:
                node = stack.pop()
                lheight, ldia = visited[node.left]
                rheight, rdia = visited[node.right]
                dia = max(ldia, rdia, lheight+rheight)
                visited[node] = (1+max(lheight,rheight), dia)
                res = max(res, dia)
        return res
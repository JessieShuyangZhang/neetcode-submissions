"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldtonew = {}
        q = deque([node])
        oldtonew[node] = Node(node.val)
        while q:
            v = q.popleft()
            for nei in v.neighbors:
                if nei not in oldtonew:
                    neinode = Node(nei.val)
                    oldtonew[nei] = neinode
                    q.append(nei)
                oldtonew[v].neighbors.append(oldtonew[nei])
        return oldtonew[node]
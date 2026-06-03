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
        mp = {} # oldNode → clonedNode
        head = Node(node.val)
        q = deque()
        q.append(node)
        mp[node] = head
        while q: 
            n = q.popleft()
            for nei in n.neighbors: 
                if nei not in mp:
                    q.append(nei)
                    mp[nei] = Node(nei.val)
                mp[n].neighbors.append(mp[nei])
                    
        return head
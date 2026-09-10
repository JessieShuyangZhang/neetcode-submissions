class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[0]] = adj.get(prereq[0],[]) + [prereq[1]]

        visiting = set()
        completed = set()

        def hascycle(node):
            if len(adj[node]) == 0:
                return False
            if node in completed:
                return False
            if node in visiting:
                return True
            visiting.add(node)
            for nei in adj[node]:
                res = hascycle(nei)
                if res:
                    return True
            visiting.remove(node)
            completed.add(node)
            return False
        
        for i in range(numCourses):
            if i not in completed:
                if hascycle(i):
                    return False
        return True
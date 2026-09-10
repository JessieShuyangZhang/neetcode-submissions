class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegrees = [0]*numCourses
        res = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        
        q = deque()
        for course, degree in enumerate(indegrees):
            if degree == 0:
                q.append(course)

        taken = set()        
        while q:
            course = q.popleft()
            taken.add(course)
            res.append(course)
            for after in adj[course]:
                indegrees[after] -= 1
                if indegrees[after] == 0:
                    q.append(after)
        if len(taken) == numCourses:
            return res
        else:
            return []
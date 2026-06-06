class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0]*numCourses
        adj = defaultdict(list)
        for i,j in prerequisites:
            indegrees[j] += 1
            adj[i].append(j)
            adj[j].append(i)
        finished = set()
        q = deque([ind for ind,degree in enumerate(indegrees) if degree==0])
        while q:
            course = q.popleft()
            finished.add(course)
            for prereq in adj[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)
        if len(finished) == numCourses:
            return True
        return False
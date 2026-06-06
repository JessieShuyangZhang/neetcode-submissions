class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0]*numCourses
        adj = defaultdict(list)
        for i, j in prerequisites:
            indegrees[j] += 1
            adj[i].append(j)
        q = deque([i for i, degree in enumerate(indegrees) if degree==0])
        res, finished = deque(),set()
        while q:
            course = q.popleft()
            if course not in finished:
                finished.add(course)
                res.appendleft(course)
                for prereq in adj[course]:
                    indegrees[prereq] -= 1
                    if indegrees[prereq] == 0:
                        q.append(prereq)
        if len(finished) != numCourses:
            return []
        else:
            return list(res)
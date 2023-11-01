# https://leetcode.com/problems/course-schedule-iv/



class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[1]] += 1
            graph[pre[0]].append(pre[1])
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        res = []
        for q in queries:
            if q[1] in graph[q[0]]:
                res.append(True)
            else:
                res.append(False)
        return res

import sys
from collections import defaultdict, deque
prerequisites = [[1,4],[2,4],[3,1],[3,2]] # expected = true
numCourses = 5
graph = defaultdict(list)
indegree = [0]*numCourses
for x,y in prerequisites:
    graph[x].append(y)
    indegree[y] += 1
    
print(indegree)
q = deque(idx for idx,val in enumerate(indegree) if val == 0)
print(q)
cnt = numCourses
while q:
    now = q.pop()
    cnt -= 1
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

if cnt > 0:
    print("False")
else:
    print("True")
    

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         graph = collections.defaultdict(list)
#         for x,y in prerequisites:
#             graph[x].append(y)
#         print(graph)
#         traced = [] 
#         visited = []
#         def dfs(now):
#             if now in visited:
#                 return True
#             if now in traced:
#                 return False
#             traced.append(now)
#             for next in graph[now]:
#                 if dfs(next) == False:
#                     return False
#             traced.remove(now)
#             visited.append(now)
        
#             return True
        
#         for x,_ in prerequisites:
#             if dfs(x) == False:
#                 return False
        
#         return True

    
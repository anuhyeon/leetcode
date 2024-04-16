import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
visited = []
result = []
graph = []
def dfs(idx):
    global k,n
    if len(visited) == k:
        result.append(visited[:])
        return
    
    for i in range(idx,n):
        if graph[i] not in visited:
            visited.append(graph[i])
            dfs(i)
            visited.pop()

    
for i in range(1,n+1):
    graph.append(i)

for i in range(n):
    visited.append(graph[i])
    dfs(i)
    visited.pop()

print(result)


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         self.n = n
#         self.k = k
#         self.result = []
#         self.visited = []
#         self.graph = []
#         for i in range(1,n+1):
#             self.graph.append(i)

#         def dfs(idx,graph,visited):
#             if len(visited) == self.k:
#                 self.result.append(visited[:])
#                 return

#             for i in range(idx,self.n):
#                 if graph[i] not in visited:
#                     visited.append(graph[i])
#                     dfs(i,graph,visited)
#                     visited.pop()
        
#         for i in range(n):
#             self.visited.append(self.graph[i])
#             dfs(i,self.graph,self.visited)
#             self.visited.pop()

#         return self.result
            
        
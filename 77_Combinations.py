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
        #if graph[i] not in visited:
            visited.append(graph[i])
            dfs(i+1)
            visited.pop()

    
for i in range(1,n+1):
    graph.append(i)

for i in range(n):
    visited.append(graph[i])
    dfs(i+1)
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

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         self.n = n
#         self.k = k
#         result = []
#         visited = []

#         def dfs(idx,visited):
#             if len(visited) == self.k:
#                 result.append(visited[:])
#                 return

#             for i in range(idx,self.n+1):
#                 if i not in visited:
#                     visited.append(i)
#                     dfs(i,visited)
#                     visited.pop()
        
#         for i in range(1,n+1):
#             visited.append(i)
#             dfs(i,visited)
#             visited.pop()

#         return result
            
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []
        
#         # 재귀 함수를 정의. 현재까지의 조합(comb)과 다음에 추가할 숫자의 시작점(start)을 인자로 받음.
#         def dfs(start, comb):
#             # 현재 조합의 길이가 k와 같으면 결과 리스트에 추가.
#             if len(comb) == k:
#                 result.append(comb)
#                 return
            
#             # start부터 n까지의 숫자를 하나씩.
#             for i in range(start, n + 1):
#                 # 현재 숫자 i를 선택하고, 다음 재귀 호출을 진행.
#                 dfs(i + 1, comb + [i])
        
#         # 재귀 함수를 호출하여 조합 탐색을 시작.
#         dfs(1, [])
        
#         return result
        
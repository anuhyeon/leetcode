import sys

graph_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

graph_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

visited_1 = [[0]*len(graph_1[0]) for _ in range(len(graph_1))]
visited_2 = [[0]*len(graph_2[0]) for _ in range(len(graph_2))]

nwes = [(1,0),(-1,0),(0,-1),(0,1)]
cnt = 0

def dfs(G,i,j,visited):
    visited[i][j] = 1
    for di,dj in nwes:
        if  0 <= i+di < len(G) and 0 <= j+dj < len(G[0]) and G[i+di][j+dj] == '1' and visited[i+di][j+dj] != 1:
            dfs(G,i+di,j+dj,visited)

def solution(G,i,j,visited):
    global cnt
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] == "1" and visited[i][j] == 0:
                dfs(G,i,j,visited)
                cnt += 1
             
    return cnt
# print(solution(graph_1,0,0,visited_1))
# print()
# print(visited_1)

print(solution(graph_2,0,0,visited_2))
print()
print(visited_2)

#[1, 1, 1, 1, 0],
#[1, 1, 0, 1, 0],
#[1, 1, 0, 0, 0], 
#[0, 0, 0, 0, 0]]
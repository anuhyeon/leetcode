#import sys
from collections import defaultdict
n = 2
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]] #[[1,0],[0,1]]
#prerequisites = [[1,0]]
visited = []
graph = defaultdict(list)
for x,y in prerequisites:
    graph[x].append(y)

print(graph)

def dfs(now): # 순환 그래프가 아니면 true 반환
    if now in visited:
        return False
    visited.append(now)
    for next in graph[now]:
            if dfs(next) == False:
                return False
    
    return True


for x,_ in prerequisites:
    #print(dfs(x))
    if dfs(x) == False:
        print(dfs(x))
        break      

#print(dfs(1))


# 추적 경로를 담을 set 생성
traced = set()
# 방문한 노드를 담을 set 생성
visited = set()

def dfs(v):
    # 이미 탐색을 마친 노드이면 dfs 종료
    if v in visited:
        return True
    # 경로에 포함되어 있는 노드이면 순환 그래프
    if v in traced:
        return False
    # 경로에 v 노드 추가
    traced.add(v)
    for w in graph[v]:
        if not dfs(w):
            return False
    # 경로에 v노드 제거
    traced.remove(v)
    # 방문한 노드에 v 추가
    visited.add(v)
    return True
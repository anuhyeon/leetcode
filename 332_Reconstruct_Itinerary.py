import sys
from collections import defaultdict
case1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
case2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
case3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# graph1 = defaultdict(list)
# for s,e in sorted(case1):
#     graph1[s].append(e)

# graph2 = defaultdict(list)
# for s,e in sorted(case2):
#     graph2[s].append(e)
    
graph3 = defaultdict(list)
for s,e in sorted(case3):
    graph3[s].append(e)
    
visited = []

# print(graph1, len(graph1))
# print(graph2, len(graph2))

def dfs(start):
    
    while graph3[start]:
        # visited.append(end)
        # graph3[start].remove(end)
        next = graph3[start].pop(0)   
        dfs(next)
    visited.append(start)

        

dfs("JFK")
print(visited[::-1])
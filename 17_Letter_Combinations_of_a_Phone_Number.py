from __future__ import annotations
import sys
from typing import Type,Any
digits = sys.stdin.readline().rstrip()
graph = { "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
    }
path = ""
nodes = [s for s in digits]
print(nodes)
result = []
def dfs(nodes,idx,path):
    if len(path) == len(nodes):
        result.append(path)
        return
    for i in range(idx,len(nodes)): 
        for j in graph[nodes[i]]:
            dfs(nodes,i+1,path+j)

    if not digits:
        return []

dfs(nodes,0,"")

print(result)
        
       

    




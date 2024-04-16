import sys 
arr = list(map(int,sys.stdin.readline().split()))
result = []
visited = []

def dfs():
    if len(visited) == len(arr):
        result.append(visited[:])
        return
    
    for i in range(len(arr)):
        if arr[i] not in visited:
            visited.append(arr[i])
            dfs() 
            visited.pop()


for i in range(len(arr)):
    visited.append(arr[i])
    dfs()
    visited.pop()
 
print(result)   
    

# def dfs(idx,arr):
#     if len(answer) == len(arr):
#         result.append(answer)
#         return
    
#     for i in range(idx,len(arr)):
#         answer.append(arr[i])
#         dfs(i+1,arr)
#         answer.pop()

    
#     return result
        
# print(dfs(0,arr))
        
import sys
candidates = list(map(int,sys.stdin.readline().split()))
target = int(sys.stdin.readline().rstrip())
visited = []
result = []
sum = 0

print(candidates,target)

def dfs(idx,sum):
    if sum == target:
        result.append(visited[:])
        return
    if sum > target:
        return
    
    for i in range(idx,len(candidates)):
            visited.append(candidates[i])
            dfs(i,sum + candidates[i])
            visited.pop()
            
dfs(0,0)
            
# for i in range(len(candidates)):
#     visited.append(candidates[i])
#     dfs(i,sum+candidates[i])
#     visited.pop()
    

print(result)
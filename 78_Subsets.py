import sys
nums = list(map(int,sys.stdin.readline().split()))
visited = []
result = []


def dfs(idx):
    result.append(visited[:])
    for i in range(idx,len(nums)):
        visited.append(nums[i])
        #result.append(visited[:])
        dfs(i+1)
        visited.pop()

# for i in range(len(nums)):
#     visited.append(nums[i])
#     result.append(visited[:])
#     dfs(i)
#     visited.pop() 
#result.append(result)   
dfs(0)
print(result)


# def dfs2(idx,path):
#     result.append(path)
    
#     for i in range(idx,len(nums)):
#         dfs2(i+1,path+[nums[i]])

# dfs2(0,[])
# print(result)
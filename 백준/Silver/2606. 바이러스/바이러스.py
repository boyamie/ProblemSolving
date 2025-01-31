import sys
input = sys.stdin.readline
num = int(input())
link = int(input())
network = [[]*(num+1) for _ in range(num+1)]
for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
visited = [0]*(num+1)
cnt = 0
def dfs(v):
    global cnt
    visited[v]=1
    for i in network[v]:
        if (visited[i]==0):
            dfs(i)
            cnt+=1
def bfs(v):
    global cnt
    visited[v]=1
    queue = [v]
    while queue:
        for i in network[queue.pop()]:
            if(visited[i]==0):
                visited[i]=1
                queue.insert(0,i)
                cnt += 1

bfs(1)
print(cnt)
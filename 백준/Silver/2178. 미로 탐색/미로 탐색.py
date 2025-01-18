import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>= n or ny >= m or nx<0 or ny<0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append([nx,ny])
    return graph[n-1][m-1]
print(bfs(0,0))
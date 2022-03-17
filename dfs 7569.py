##7576문제의 3차원버전
from collections import deque
import sys

input = sys.stdin.readline
m, n, h = map(int, input().split())

# 3차원 list input
matrix = [[list(map(int,input().split())) for _ in range(n)]for _ in range(h)]

queue = deque()

a, b, c = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]

cnt = 0

def bfs():
  while queue:
    #큐에있는 토마토 pop
    z,x,y = queue.popleft()
    for i in range(6):
      nextx, nexty, nextz = x+a[i], y+b[i], z+c[i]
      if 0 <= nextx < n and 0 <= nexty < m and 0 <= nextz < h and matrix[nextz][nextx][nexty] == 0:
        matrix[nextz][nextx][nexty] = matrix[z][x][y] + 1
        queue.append([nextz,nextx,nexty])

for i in range(h):
  for j in range(n):
    for k in range(m):
      if matrix[i][j][k] == 1:
        queue.append([i,j,k])

bfs()
flag = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if matrix[i][j][k] == 0:
        flag = 1
      cnt = max(cnt, matrix[i][j][k])

if flag == 1:
  print(-1)
elif cnt == 1:
  print(0)
else:
  print(cnt-1)

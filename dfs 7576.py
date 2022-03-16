#dfs를 사용하기위해 queue를 이용할것임
from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

#2차원 list를 input
matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

#더하고빼주기
x, y = [-1,1,0,0], [0,0,-1,1]

cnt = 0

def bfs():
  while queue:
    #큐에있는 토마토 pop
    a, b = queue.popleft()
    #익힐토마토찾기
    for i in range(4):
      nexta, nextb = x[i] + a, y[i] + b
      
      if 0 <= nexta < n and 0 <= nextb < m and matrix[nexta][nextb] == 0:
        #익히고 1 더해주면서 횟수 세기,, 제일 큰값이 정답이됨
        matrix[nexta][nextb] = matrix[a][b] + 1
        queue.append([nexta,nextb])


for i in range(n):
  for j in range(m):
    #익은 토마토가 좌표에 있을때
    if matrix[i][j] == 1:
      queue.append([i,j])

bfs()

for i in matrix:
  for j in i:
    #토마토를 다 익히지 못했다면 -1 출력 
    if j == 0:
      print(-1)
      exit(0)
  #다익혔으면 최댓값이 정답
  cnt = max(cnt, max(i))
print(cnt-1)

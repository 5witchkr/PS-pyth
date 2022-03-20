from collections import deque
import sys

#n개 줄 m개 숫자
n, m = map(int, input().split())

L = []

for _ in range(n):
  L.append(list(map(int, input().replace("\n",""))))

#bfs (너비우선탐색)
def bfs(x, y):
  #상하좌우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  #queue
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    #4방향
    for i in range(4):
      nextx = x + dx[i]
      nexty = y + dy[i]
      #범위체크
      if nextx < 0 or nextx >= n or nexty < 0 or nexty >= m:
        continue
      #벽 체크
      if L[nextx][nexty] == 0:
        continue
      #이동가능
      if L[nextx][nexty] == 1:
        L[nextx][nexty] = L[x][y] + 1
        queue.append((nextx,nexty))
  #
  return L[n-1][m-1]

print(bfs(0,0))

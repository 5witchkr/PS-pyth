import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
lst = [0 for _ in range(n+1)]#진입차수
queue = deque()
answer = []

for i in range(m):
  a, b = map(int, input().rstrip().split())
  graph[a].append(b)
  lst[b] += 1


#위상정렬 알고리즘
for i in range(1, n+1):
  if lst[i] == 0:
    queue.append(i)
  
while queue:
  now = queue.popleft()
  answer.append(now)
  for i in graph[now]:
    lst[i] -= 1
    if lst[i] == 0:
      queue.append(i)

print(*answer)

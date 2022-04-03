## 시작점부터 끝점까지 최단거리로 방문하되,
## v1과 v2를 무조건 방문해줘야함
## ex> start - v1 - v2 - N
## ex> start - v2 - v1 - N

##구현?
##1> start - v1 , start -v2  다익스트라
##2> v1 - v2 양방향 다익스트라
##3> v2 - N 다익스트라 (v1 - N은 2번에서 이미 ㅇ)

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

#다익스트라
def distra(start, end):
  dis = [0xffffff] * (N+1)
  dis[start] = 0
  q = [[0, start]]
  while q:
    k, u = heappop(q)
    if k > dis[u]:
      continue
    for w, v in G[u]:
      if dis[v] > dis[u] +w:
        dis[v] = dis[u] +w
        heappush(q, [dis[v],v])
  return dis[end]

N, E = map(int,input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  G[u].append([w,v])
  G[v].append([w,u])

stop1, stop2 = map(int,input().split())

path1 = distra(1,stop1) + distra(stop1,stop2) + distra(stop2,N)

path2 = distra(1,stop2) + distra(stop2,stop1) + distra(stop1,N)

if path1 >= 0xffffff and path2 >= 0xffffff:
  print(-1)
else:
  print(min(path1,path2))

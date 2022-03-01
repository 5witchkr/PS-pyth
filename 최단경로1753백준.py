#다익스트라 알고리즘..?
#각 정점을 돌면서 최소값으로 갱신해주는 알고리즘

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)#재귀많이돌것임
import heapq

n, m = map(int, input().split())# 정점의 개수 n, 간선의 개수 m

k = int(input())# 시작 정점의 번호

INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]#전체 그래프
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)#갱신 할 그래프, 정점의 갯수만큼 만들어줌 초기값은 INF

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())#C는 비용 a,b는 연결되어있음
    # a->b가 c비용
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0##시작지점은 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(k)#k로 시작

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:##inf는 갈수없는곳. distance그래프에서 갱신이 한번도 되지 않은값이기때문
        print("INF")
    else:
        print(distance[i])##해당 정점의 최소거리를 출력
        
        
import sys
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split())##v는 정점, e는 간선
k = int(sys.stdin.readline())#시작지점
    
L = [[] for _ in range(v + 1)]#전체그래프
dp = [inf] * (v + 1)#갱신 할 그래프 ,정점의 갯수만큼 만들어줌 초기값은 INF
heap = []

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())#u, v 는 이어진 정점 w는 사이 거리
    L[u].append([v, w])##L[u]에 이어진 정점과 거리를 넣어줌
    
def dijkstra(start):
    dp[start] = 0#시작지점은 거리가 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)#가장 최단 거리가 짧은 노드에 대한 정보
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

dijkstra(k)

for i in dp[1:]:
    print(i if i != inf else "INF")

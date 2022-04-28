#백준 13549
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

#deque
q = deque()
#방문기록
vis = [-1] * 200001

q.append(N)
vis[N] = 0

while q:
    x = q.popleft()
    if x == M:
        ##같으면 출력
        print(vis[x])
        sys.exit()
    #순간이동해서 갈수있는곳을 구함
    #200000보다작고 방문하지않았을때
    if x*2 <= 200000 and vis[x*2] == -1:
        vis[x*2] = vis[x]
        #appendleft로 큐의 앞에 넣어서 해당 초에 방문할수있도록 함
        q.appendleft(x*2)
    #x-1로 갈수있는곳 1초 더한다
    # 0보다 크고 방문하지 않았을때
    if x-1 >= 0 and vis[x-1] == -1:
        vis[x-1] = vis[x] +1
        q.append(x-1)
    #x+1 로 갈수있는곳 1초 더함
    # 200000보다 작고 방문하지않았을때
    if x+1 <= 200000 and vis[x+1] == -1:
        vis[x+1] = vis[x]+1
        q.append(x+1)

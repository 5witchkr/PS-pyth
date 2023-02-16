```python
from collections import deque
from sys import stdin
from collections import defaultdict

## 정점갯수, 간선갯수, 탐색 시작 정점

vertex_count, edge_count, vertex_start \
    = map(int, stdin.readline().strip().split())



## init graph
graph = [[] for i in range(vertex_count+1)]

## init visited graph
visited_dfs = [False] * (vertex_count+1)
visited_bfs = [False] * (vertex_count+1)

#input value
for i in range(edge_count):
    a, b = map(int, stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()


def bfs(V):
    q = deque([V])
    visited_bfs[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in graph[V]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True


def dfs(V):
    visited_dfs[V] = True
    print(V, end=" ")
    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(i)

dfs(vertex_start)
print()
bfs(vertex_start)
```

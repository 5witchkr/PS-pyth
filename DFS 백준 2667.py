#DFS 사용
import sys

n = int(sys.stdin.readline().replace("\n",""))

L = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []

for i in range(n):
    L.append(list(sys.stdin.readline().replace("\n","")))

def DFS(i, j):
    queue = [[i, j]]
    L[i][j] = "0"
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and L[x][y] == "1":
                L[x][y] = "0"
                queue.append([x, y])
                count += 1
    cnt.append(count)

for i in range(n):##가로와 세로의 길이는 같음
    for j in range(n):
        if L[i][j] == "1":
            DFS(i, j)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

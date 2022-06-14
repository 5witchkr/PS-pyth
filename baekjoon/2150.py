import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

M = {}
for i in range(n):
    M[i] = []

cnt = 0
dfsnum = [0] * n
finish = [0] * n
stack = []
scc = []

for _ in range(m):
    a, b = map(int, input().split())
    #a -> b 연결
    M[a-1].append(b-1)


def dfs(x):
    global cnt
    cnt += 1
    dfsnum[x] = cnt
    stack.append(x)
    par = dfsnum[x]

    for i in M[x]:
        #방문하지 않은이웃
        if dfsnum[i] == 0:
            par = min(par, dfs(i))
        #처리중인 이웃
        elif finish[i] == 0:
            par = min(par, dfsnum[i])
    #부모노드 == 현재노드
    if par == dfsnum[x]:
        iSCC = []
        while True:
            t = stack.pop()
            iSCC.append(t+1)
            finish[t] = 1
            if t == x:
                break
        scc.append(sorted(iSCC))
    return par

## n개만큼 dfs
for i in range(n):
    if dfsnum[i] == 0:
        dfs(i)
print(len(scc))
for i in sorted(scc):
    print(*i, -1)

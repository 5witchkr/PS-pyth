import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

M = {}
for i in range(n+1):
    M[i] = []


vi = [0] * (n+1)

#map에 넣어줌
for _ in range(m):
    a, b = map(int, input().split())
    M[a].append(b)
    M[b].append(a)


def check(M, v, vi):
    vi[v] = 1
    for i in M[v]:
        if vi[i] != 1:
            check(M, i, vi)

check(M, 1, vi)

print(sum(vi)-1)

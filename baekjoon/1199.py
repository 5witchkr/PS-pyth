import sys
sys.setrecursionlimit(10**9)

N=int(sys.stdin.readline())

L=[]

for i in range(N):
   L.append(list(map(int,sys.stdin.readline().rstrip().split())))

graph={}

for i in range(N):
    graph[i]=[]
    rowSum=0
    for j in range(N):
        for k in range(L[i][j]):
            rowSum+=1
            graph[i].append(j)
    if rowSum%2==1:
        print(-1)
        sys.exit()

def dfs(nowNode):
    for i in graph[nowNode]:
        if L[nowNode][i]:
           L[nowNode][i]-=1
            L[i][nowNode]-=1
            dfs(i)
    print(nowNode+1,end=" ")

dfs(0)

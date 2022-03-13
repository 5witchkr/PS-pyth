import sys
input = sys.stdin.readline
n, k = map(int,input().split())
L = [[0,0]]#?

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
  L.append(list(map(int,input().split())))


for i in range(1,n+1):
  for j in range(1, k+1):
    w = L[i][0]#무게 가져오기
    v = L[i][1]#값 가져오기
    if j < w:#무게보다 작으면
      dp[i][j] = dp[i-1][j]#위값그대로가져옴
    else:#아니면 큰값으로 바꿔줌
      dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
print(dp[n][k])

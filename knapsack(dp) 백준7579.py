##knapsack
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
##메모리를 배열로 저장
memory = list(map(int, input().split()))
#활성화 추가비용 배열로 저장
cost = list(map(int, input().split()))



maxCost = (sum(cost)+1)
## 최고비용은 모든앱의 합이므로 sum(cost)+1 을 열개수로 설정함
dp = [[0] * maxCost for _ in range(n+1)]
listmin = maxCost

#dp배열의 행은 앱, 열은 비용을 나타냄
for i in range(1,n+1):
  for j in range(len(dp[0])):
    if j < cost[i-1]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost[i-1]]+ memory[i-1])
    #값이 확보할 메모리 m보다 크다면 j로 초기화
    if dp[i][j] >= m and listmin > j:
      listmin = j

print(listmin)

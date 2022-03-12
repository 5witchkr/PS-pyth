import sys
sys.setrecursionlimit(100000)#함수재귀제한풀기
input = sys.stdin.readline

#연결밭 모두 확인하는 함수
def dfs(x, y):
  visit[x][y] = True#현재위치 방문처리
  d = [(-1,0),(1,0),(0,-1),(0,1)]#더해주거나 빼줄것임
  for dx, dy in d:
    nx, ny = x+dx, y+dy#nx와 xy는 d를 각각 +,- 하는것 for문
    if nx < 0 or nx >= w or ny < 0 or ny >= l:#범위벗어나면예외처리
      continue
    if mtr[nx][ny] and not visit[nx][ny]:##nx,ny좌표가 방문안했으면 다시 함수실행해서 방문처리하기
      dfs(nx, ny)


t = int(input())
for _ in range(t):
  w, l, k = map(int,input().split())
  mtr = [[0]*l for _ in range(w)]#배추가있으면 1 없으면 0
  visit = [[False] * l for _ in range(w)]#방문결과
  for _ in range(k):
    x, y = map(int,input().split())
    mtr[x][y] = 1#배추
  result = 0
  #모든 밭 확인
  for i in range(w):
    for j in range(l):
      if mtr[i][j] and not visit[i][j]:#배추가있는데 방문안했다면
        dfs(i,j)#연결지역 모두 방문
        result += 1
  print(result)

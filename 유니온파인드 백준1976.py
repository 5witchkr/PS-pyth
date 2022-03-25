import sys
input = sys.stdin.readline

n = int(input())#노드 수
m = int(input())#정점 수
table = [0] * (n+1) #테이블 초기화

#테이블 상 설정
for i in range(1, n+1):
  table[i] = i

#a노드의 테이블노드 찾기
def find(x):
  if x == table[x]:#x노드가 테이블노드면 x반환
    return x
  p = find(table[x])#x노드를 따라가면서 테이블노드 찾기
  table[x] = p#테이블 갱신
  return table[x]

#x집합과 y집합 합치기
def union(x, y):
  x = find(x)#x노드의 테이블노드찾기
  y = find(y)#y노드의 테이블노드찾기
  if x < y:#x의테이블이 y테이블보다 상위루트면
    table[y] = x#y의 테이블을 x의 테이블로 변경함
  else:# y테이블이 x테이블보다 상위루트면
    table[x] = y#x테이블을 y의테이블로 변경

#y번째 도시
for y in range(1,n+1):
  maps = list(map(int, input().split()))#어느도시와 연결돼있는지 정보
  #y도시 연결정보 추출
  for x in range(1, len(maps)+1):
    if maps[x-1] == 1:#x도시랑 연결되어있으면
      union(y,x)#두 도시를 결합한다.

tour = list(map(int, input().split()))#여행계획정보 입력
result = set([find(i) for i in tour])#여행 계획의 루트노드 찾기

if len(result) != 1:#set개수가 2개이상이라면 집합이 존재함
  print('NO')
else:
  print('YES')#set개수1개면 한개집합존재

import sys
input = sys.stdin.readline


#find
def find(x):
  if parent[x] == x:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return p

#union
def union(x,y):
  x, y = find(x), find(y)
  if x != y:
    parent[y] = x
    number[x] += number[y]
  print(number[x])

 
#testcase
for _ in range(int(input())):
  #갯수
  num = int(input())
  parent, number = {}, {}
  for i in range(num):
    # a, b 입력
    a,b = input().split()
    if a not in parent:
      parent[a] = a
      number[a] = 1
    if b not in parent:
      parent[b] = b
      number[b] = 1
    union(a,b)

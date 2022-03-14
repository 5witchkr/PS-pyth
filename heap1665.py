import sys
import heapq
input = sys.stdin.readline
n = int(input())

##left와 right heap을 만들어줌
left = []
right = []
answer = []

for i in range(n):
  numb = int(input())
  if len(left) == len(right):##길이가 같으면 중간값의 기준이되는 left에 수를 넣음
    heapq.heappush(left, (-numb, numb))
  else:##길이가 다르면 길이를 맞춰주기위해 right에 수를 넣음
    heapq.heappush(right, (numb, -numb))

  if right and left[0][1] > right[0][0]:#left루트가right루트보다 크면 두 루트를 바꿔줌 (left는 중간값을 기준으로 작은수가 들어가는곳임, left가 right보다 크면 중간값보다 큰 수 가 left에 들어가는상황이라서 바꿔줘야함)
    min = heapq.heappop(right)[0]
    max = heapq.heappop(left)[1]
    heapq.heappush(left, (-min, min))
    heapq.heappush(right, (max, max))
    
  answer.append(left[0][1])

for i in answer:
  print(i)

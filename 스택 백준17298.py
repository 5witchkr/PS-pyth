import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
stack = []
##오큰수가 없으면 -1을 출력함
answer = [-1 for i in range(n)]

for i in range(len(L)):
  #stack 값이 있고 and L[스택맨위]가 L[i보다 작다면 반복한다.]
  while stack and L[stack[-1]] < L[i]:
    #answer의 stack.pop한 인덱스자리에 L[i]를 넣어줌
    answer[stack.pop()] = L[i]
  #stack에 i를넣는다.
  stack.append(i)
#*을 붙여주면 공백을 기준으로 원소들만 나열
print(*answer)

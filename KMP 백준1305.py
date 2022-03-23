import sys
input = sys.stdin.readline

# 광고판 길이
L = int(input())
# 광고 문자열
n = input().rstrip()

#실패함수(kmp패턴 부분일치테이블)
def kmp(n):
  le = len(n)
  table = [0] * le
  j = 0
  for i in range(1,le):
    while j > 0 and n[i] != n[j]:
      j = table[j -1]
    if n[i] == n[j]:
      j += 1
      table[i] = j
  return table

#가장 짧은 광고 길이를 출력
print(L - kmp(n)[-1])

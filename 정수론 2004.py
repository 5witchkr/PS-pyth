import sys
input = sys.stdin.readline

n, m = map(int,input().split())

def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

five = count(n, 5) - count(m, 5) - count(n - m, 5)
two = count(n, 2) - count(m, 2) - count(n - m, 2)

a = min(five, two)
print(a)

```
#수학공식을 이용하여 푸는문제, 거듭제곱근까지만 for문을 돌려줘야 시간초과가 나지않는다.
```
import sys
import math

t = int(sys.stdin.readline())
L = []
L2 = []
gcd = 0

for i in range(t):
    L.append(int(sys.stdin.readline()))
    if i == 1:
        gcd = abs(L[1] - L[0])##math abc : 절대값
    gcd = math.gcd(abs(L[i] - L[i-1]), gcd)##math gcd : 파라미터의 최대공약수

gcd1 = int(gcd ** 0.5)###거듭제곱근까지만 for문을 돌려주기 위함 (시간초과남)

for i in range(2, gcd1 + 1):##거듭제곱근으로 for문
    if gcd % i == 0:
        L2.append(i)
        L2.append(gcd // i)

L2.append(gcd)
L2 = list(set(L2))
L2.sort()

for i in L2:
    print(i, end=' ')

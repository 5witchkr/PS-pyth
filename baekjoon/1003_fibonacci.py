import sys
input = sys.stdin.readline

def fibonacci(N):
    #0 출력을 담는 리스트
    L0 = [1,0,1]
    #1 출력을 담는 리스트
    L1 = [0,1,1]
    if N > 2:
        for i in range(2, N):
            # 0과1을 출력하는 list에 각각 (현재항+이전항)을 추가해준다 (fibonacci)
            L0.append(L0[i] + L0[i-1])
            L1.append(L1[i] + L1[i-1])
    # N번째네 0 과 1이 출력되는 횟수를 출력해줌
    print(f'{L0[N]} {L1[N]}')


T = int(input())
for _ in range(T):
    N = int(input())
    fibonacci(N)

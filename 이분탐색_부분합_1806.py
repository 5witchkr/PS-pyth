import sys

N, S = map(int,sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().split()))

start, end, sum = 0, 0, 0
countMin = 100001

##부분합이란...? start번째 인덱스와 end번째 인덱스의 합!
##이 문제에서는 최소 부분합을 구하는문제 즉 연속으로 몇개 더해야 S이상이 되는지 구해야한다.

while True:
    # sum이 S이상이 되면 start를 하나 증가시킴
    if sum >= S:##즉 부분합이 S이상이 된 조건을 충족
        sum -= L[start]   # start의 위치 1 증가
        start += 1
        countMin = min(countMin, end - start + 1) #start~end까지 길이가 현재 최소값(countMin)보다 작으면 값갱신
    else:
        if end == N:    # end=N되면 탐색 종료
            break
        else:
            sum += L[end]     # end 위치 1 증가(꼬리늘리기)
            end += 1

if countMin == 100001:  # 초기 countMin값과 같다면 sum이 S를 넘지 못한것
    countMin = 0
print(countMin)

def sieve(n):                       # n 보다 작은 소수 리스트 구하기
    ca = list(range(2,n))
    i = 0                           # i 는 확인된 소수에 대한 인덱스
    while i < len(ca):
        p = ca[i]                   # p 는 소거되지않은 ca의 처음부터~
        j = i + 1                   # 다시 j 세팅
        while j < len(ca):
            if ca[j] % p == 0:        # p 로 나눴을때 나머지가0이면
                ca.pop(j)           # 나눠떨어지면 소거
            else:
                j = j + 1           # 아니면 다음숫자를 p로 나눔

        i = i + 1                   # 다음 p 로 가기위해 i 증가
    return ca


A = 1000
print(len(sieve(A)))
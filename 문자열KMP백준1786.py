#참고블로그https://developmentdiary.tistory.com/455
import sys
##KMP 알고리즘 사용할것임
T = sys.stdin.readline().replace("\n","")##문자열 입력 (찾는곳) replace는 뒤에 공백(\n)을 없애주는역할
P = sys.stdin.readline().replace("\n","")##패턴 입력 (찾을것)

L = [0 for _ in range(len(P))]##P의 길이만큼 0배열 생성 (지표역할) - 부분일치테이블임


def kmp(T,P,L):##kmp 함수
    j = 0
    for i in range(1,len(P)):## 찾을것의 길이만큼
        while j > 0 and P[i] != P[j]:##다를때
            j = L[j-1]##맞은부분까지 돌아가서 처음부터 다시 비교
        if P[i] == P[j]:##같을때
            j += 1##j를 1증가
            L[i] = j##i인덱스 테이블을 갱신함
    j = 0## j를 다시 리셋
    count = 0
    result = []
    lenP = len(P)
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:##다를때
            j = L[j-1]##맞은부분까지 돌아가서 다시 비교
        if T[i] == P[j]:##같을때
            if j == lenP-1:##P의 길이와 같은곳까지 같다면
                count += 1##일치갯수추가
                result.append(i-lenP+2)##결과의 위치 추가
                j = L[j]##위치를 옮기고 다시 탐색
            else:
                j += 1
    return count,result

count, result = kmp(T,P,L)

print(count)
for i in result:
    print(i,end=' ')

import sys
input = sys.stdin.readline
S = []
L = []
n = int(input())
cunt = 1
noprint = 0
for _ in range(n):
    num = int(input())
    while cunt <= num:###해당 숫자까지 cunt + 그리고 L에 "+" 추가
        S.append(cunt)## tip 카운트는 계속 1씩 증가한다. 예를들어 3이 S.pop이 되더라도 다음 카운트 4가 S에 append 된다. 
        L.append("+")
        cunt += 1

    if S[-1] == num:#스택에 마지막요소가 해당숫자와 같아지면
        S.pop()
        L.append("-")
    else:
        print("NO")
        noprint = 1
        break
if noprint == 0:
    for i in L:
        print(i)

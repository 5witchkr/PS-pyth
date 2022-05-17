import sys
input = sys.stdin.readline


def L_in_S(List, Set):
    for i in List:
        i_in_Set(i, Set)


def i_in_Set(n, Set):
    if Set & {n}:
        print(1)
    else:
        print(0)


n = input()
S = set(map(int, input().split()))
m = input()
L = list(map(int, input().split()))

L_in_S(L, S)

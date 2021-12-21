N = int(input())
for _ in range(N):
    A = int(input())
    B = int(input())
    C = list(range(1,B+1))
    j = 0
    while j < A:

        for i in range(1,len(C)):
            C[i] = C[i-1] + C[i]
        j += 1
    print(C[len(C)-1])


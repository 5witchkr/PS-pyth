def bubblesort(a):
    sort = False
    while not sort:
        sort = True
        for i in range(1,len(a)):
            if a[i-1] > a[i]:
                a[i-1],a[i] = a[i],a[i-1]
                sort = False

A = [4,5,7,10,11,1,9]
bubblesort(A)
print(A)
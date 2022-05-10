def splitPlus(list):
    listEliment = []

    for i in list:
        listEliment.append(plusListEliment(i.split('+')))

    return listEliment


def plusListEliment(list):
    plusEliment = 0

    for k in list:
        plusEliment += int(k)

    return plusEliment


def totalvalue(list):
    firstEliment = list[0]
    otherEliment = 0

    for i in list[1:]:
        otherEliment -= i

    return firstEliment + otherEliment



n = input().split('-')

print(totalvalue(splitPlus(n)))


#풀이 2
#
# n = input().split('-')

# result = 0

# resultlist = []
# for i in n:
#     j = i.split('+')
#     for k in j:
#         result += int(k)
#     resultlist.append(result)
#     result = 0

# result = resultlist[0]

# for i in resultlist[1:]:
#     result -= i

# print(result)

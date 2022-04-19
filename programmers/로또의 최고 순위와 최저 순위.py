def solution(lottos, win_nums):

    lottosSet = set(lottos)
    win_numsSet = set(win_nums)

    rst = lottosSet.intersection(win_numsSet)

    rate = [6,6,5,4,3,2,1]
    maxval = len(rst) + lottos.count(0)
    minval = len(rst)


    answer = [rate[maxval], rate[minval]]
    return answer

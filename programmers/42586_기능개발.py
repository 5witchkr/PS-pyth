
  ##큐스택 활용코드
  
def solution(progresses, speeds):
    list = []
    queue = []
    answer = []
    for i in range(len(progresses)):
        k = 1
        while (100 > speeds[i] * k + progresses[i]):
            k += 1
        list.append(k)
        
    queue.append(list[0])
        
    for i in list[1:]:
        if i > queue[0]:
            answer.append(len(queue))
            queue = []
            queue.append(i)       
        elif i <= queue[0]:
            queue.append(i)
    answer.append(len(queue))
    
    return answer

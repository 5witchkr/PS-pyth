##단순통과코드
def solution(progresses, speeds):
    stack1 = []
    answer = []
    count = 1
    for i in progresses:
        done = 100-i
        k = -1
        while done >= 0:
            k += 1
            done-=speeds[progresses.index(i)]
        stack1.append(k)

    for i in range(1,len(stack1)):
        if stack1[i-1] >= stack1[i]:
            count+=1
        else:
            answer.append(count)
            count = 1
    answer.append(count)
    
    return answer
  
  ##큐스택 활용코드
  

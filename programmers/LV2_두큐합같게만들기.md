- `시간초과`로 틀렸다.

 ```python
 from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    answer = 0

    while sum(queue1) != sum(queue2):
        if sum(queue1) > sum(queue2):
            queue2.append(queue1.popleft())
            answer+=1
        if sum(queue2) > sum(queue1):
            queue1.append(queue2.popleft())
            answer+=1
        if answer == limit:
            answer = -1
            break

    return answer
```

- sum에 소요되는 시간복잡도를 고려해서 줄여본 뒤 제출해봤다.

```python
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    sumQueue1 = sum(queue1)
    sumQueue2 = sum(queue2)
    answer = 0


    while sumQueue1 != sumQueue2:
        if sumQueue1 > sumQueue2:
            popNumber = queue1.popleft()
            queue2.append(popNumber)
            answer+=1
            sumQueue1 -= popNumber
            sumQueue2 += popNumber
            
        if sumQueue2 > sumQueue1:
            popNumber = queue2.popleft()
            queue1.append(popNumber)
            answer+=1
            sumQueue1 += popNumber
            sumQueue2 -= popNumber
            
        if answer == limit:
            answer = -1
            break

    return answer
```

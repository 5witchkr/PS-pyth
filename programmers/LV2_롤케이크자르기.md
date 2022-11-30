```python
def solution(topping):
    answer = 0
    for i in range(1, len(topping)):
        A = topping[0:i]
        B = topping[i:len(topping)]
        if len(set(A)) == len(set(B)):
            answer +=1
    return answer
```
- `시간초과`로 틀렸다.


- 통과코드
```python
from collections import Counter

def solution(topping):
    answer = 0
    dicA = Counter(topping)
    dicB = set()
    for num in topping:
        dicA[num] -= 1
        dicB.add(num)
        if dicA[num] == 0:
            dicA.pop(num)
        if len(dicA) == len(dicB):
            answer+=1
    return answer
```

- 고민 좀 하다가 다른사람 코드를 보니 Counter를 이용했길래 참고했다.



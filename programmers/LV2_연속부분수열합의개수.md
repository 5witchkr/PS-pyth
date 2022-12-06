- set을 이용
- 
```python
def solution(elements):
    elementsSize = len(elements)
    elements = elements+elements
    answer = set()
    for i in range(elementsSize):
        for j in range(elementsSize):
            answer.add(sum(elements[i:j+i+1]))
    return len(answer)
```

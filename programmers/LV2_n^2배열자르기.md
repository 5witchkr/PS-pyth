- 2중 for문으로 접근 -> `시간초과`
- 다른사람 풀이 참고
- 해당 위치 값 = max(해당 위치 // n, 해당 위치 % n) + 1

```python
def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
            
    return answer
```

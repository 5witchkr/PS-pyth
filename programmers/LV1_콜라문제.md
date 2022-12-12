- 단순한 산술연산문제
```python
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += n//a * b
        n = n//a * b + n % a
    return answer
```

- 첫시도에 `시간초과`로 틀렸다

```python
numberSize, sumCount = map(int, input().split())
numbers = list(map(int, input().split()))

def sumfun(start, end):
    global numbers
    result = 0
    for i in numbers[start:end]:
        result += i
    return result

for _ in range(sumCount):
    startNum, endNum = map(int, input().split())
    print(sumfun(startNum-1, endNum))
```

- `prefix_sum` 이용, stdin.readline()이용 -> `통과`
- 여러번 계산해야하는 수들을 미리 한번만 계산한 뒤 return하는 방식으로 구현

```python
from sys import stdin

numberSize, sumCount = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
prefix = [0]
sumNum = 0
for num in numbers:
    sumNum += num
    prefix.append(sumNum)

for _ in range(sumCount):
    startNum, endNum = map(int, stdin.readline().split())
    print(prefix[endNum] - prefix[startNum - 1])
```

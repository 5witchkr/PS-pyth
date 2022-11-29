```python
from collections import Counter

def solution(want, number, discount):
    answer = 0
    ## list to dic
    dic = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        thisDiscount = discount[i:i+10]
        if Counter(thisDiscount) == dic:
            answer += 1
    return answer
```

- 문제를 잘못읽고 틀렸었다.
- 실행 `결과값`을 일치하는 날짜가 아닌, `총 일수를 리턴`해야한다.
- 한동안 ps에 손을 놓고있었는데 파이썬으로 문법 찾아가며 해보니 파이썬 유틸이 진짜 깡패인것같다..

![화면 캡처 2022-11-29 211736](https://user-images.githubusercontent.com/95848796/204527390-522201ed-3bac-4316-b55d-f95d8c3f7da4.png)

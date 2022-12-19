```python
def solution(lottos, win_nums):
    bonus = lottos.count(0)               
    winCount = 0                               
    match = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}           
                                         
    for l in lottos:                    
        if l in win_nums:
            winCount += 1
    
    best = winCount + bonus                    
    worst = winCount                          
    return [match[best], match[worst]]
 ```

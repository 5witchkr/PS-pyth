##KMP 활용문제
while True:
  n = input()
  if n == ".":###.이면 빠져나가기
    break
  else:
    table = [0 for _ in range(len(n))]##table생성

    # j는 실패함수
    j = 0
    for i in range(1,len(n)):
      while j>0 and n[i] != n[j]:
        j = table[j-1]
      if n[i] == n[j]:
        j += 1
        table[i] = j
        
        
    if len(n) % (len(n) - table[len(n)-1]) == 0:###패턴의 길이로 len(n)이 나누어떨어지면
      print(len(n)//(len(n) - table[len(n)-1]))##나누어 떨어지는거 출력
    else:
      print(1)##반복되는 패턴이 없으므로 1출력

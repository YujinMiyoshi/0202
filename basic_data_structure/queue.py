from collections import deque

n, q = list(map(int, input().split()))

pro_time = deque([])
finished = []
sum_time = 0

for i in range(n):
  pro, time = list(input().split())
  time = int(time)
  sum_time += time
  pro_time.append([pro, time])
  
first_time = sum_time

while sum_time > 0:
  val = pro_time.popleft()
  val[1] = val[1] - q
  sum_time -= q
  
  if val[1] <= 0:
    sum_time -= val[1]
    end_time = first_time - sum_time
    finished.append([val[0], end_time])
    
  else:
    pro_time.append(val)
    
for i in finished:
  print(i[0], i[1])    
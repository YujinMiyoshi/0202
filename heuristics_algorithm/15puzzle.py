import queue
import copy

que = queue.Queue()
visit = []
init = []
ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
relate =[[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11],
            [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15], [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]

for i in range(4):
  vals = list(map(int, input().split()))
  
  for val in vals:
    init.append(val)
    
que.put([init, 0])
visit.append(init)

while que:
  s, c = que.get()
  
  if s == ans:
    print(c)
    break

  sc = s
  
  space = sc.index(0)
  
  for i in relate[space]:
    num = sc[i]
    
    sc2 = copy.copy(sc)
    
    for j in range(16):
      if sc2[j] == 0:
        sc2[i], sc2[j] = sc2[j], sc2[i]
        break
    
    if sc2 in visit:
      continue
    
    visit.append(sc2)
    
    que.put([sc2, c + 1])
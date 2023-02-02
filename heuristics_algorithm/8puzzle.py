import queue

que = queue.Queue()
visit = []
init = ''
ans = '123456780'
relate =[[1,3], [0,2,4], [1,5], [0, 4, 6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]

for i in range(3):
  vals = list(map(int, input().split()))
  
  for val in vals:
    val = str(val)
    init += val
    
que.put([init, 0])
visit.append(init)

while que:
  s, c = que.get()
  
  if s == ans:
    print(c)
    break

  sc = s
  
  space = sc.find('0')
  
  for i in relate[space]:
    num = sc[i]
    sc2 = sc.replace(num, 'x').replace('0', num).replace('x', '0')
    
    if sc2 in visit:
      continue
    
    visit.append(sc2)
    
    que.put([sc2, c + 1])
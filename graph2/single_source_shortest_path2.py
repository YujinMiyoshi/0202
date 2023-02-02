from heapq import heapify, heappop, heappush

class priority_queue:
  def __init__(self, heap):
    self.heap = heap
    heapify(self.heap)
    
  def push(self, item):
    heappush(self.heap, item)
    
  def pop(self):
    return heappop(self.heap)

  def __len__(self):
        return len(self.heap)
  
inf = 10**6
state = []
distance = []
parent = []

n = int(input())
v = 0

matrix = [[inf]*n for i in range(n)]

for i in range(n):
  e = list(map(int, input().split()))
  
  if e[1] != 0:
    u = e[0]
    
    for k, j in enumerate(e[2:], 2):
      if k % 2 == 0:
        v = j
      else:
        matrix[u][v] = j
  
  state.append(0)
  distance.append(inf)
  parent.append(-1)

distance[0] = 0
  
pq = priority_queue([(0, 0)])
  
while pq:
  min, u = pq.pop()

  state[u] = 2
  
  if distance[u] < min:
    continue
  
  for v in range(n):
    if state[v] != 2 and matrix[u][v] != inf:
      if distance[u] + matrix[u][v] < distance[v]:
        distance[v] = distance[u] + matrix[u][v]
        parent[v] = u
        state[v] = 1
        pq.push((distance[v], v))
        
for i in range(n):
  print(i, distance[i])
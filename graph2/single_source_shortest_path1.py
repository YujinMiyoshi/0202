inf = 10**6
state = []
dict = []
parent = []

n = int(input())

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
  dict.append(inf)
  parent.append(-1)
  
dict[0] = 0

while True:
  min = inf
  
  for i in range(n):
    if state[i] != 2 and dict[i] < min:
      min = dict[i]
      u = i
      
  if min == inf:
    break
  
  state[u] = 2
  
  for v in range(n):
    if state[v] != 2 and matrix[u][v] != inf:
      if dict[u] + matrix[u][v] < dict[v]:
        dict[v] = dict[u] + matrix[u][v]
        parent[v] = u
        state[v] = 1
        
for i in range(n):
  print(i, dict[i])
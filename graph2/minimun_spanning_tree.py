inf = 10**6
matrix = []
state = []
dict = []
parent = []
sum = 0

n = int(input())

for i in range(n):
  e = list(map(int, input().split()))
  
  for i in range(len(e)):
    if e[i] == -1:
      e[i] = inf
      
  matrix.append(e)
  
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
      if matrix[u][v] < dict[v]:
        dict[v] = matrix[u][v]
        parent[v] = u
        state[v] = 1
          
for i in range(n):
  if parent[i] != -1:
    sum += matrix[i][parent[i]]
    
print(sum)
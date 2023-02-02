def visit(u):
  global time
  state[u] = 1
  time += 1
  visited[u] = time
      
  for v in range(n):
    if L[u][v] == 0:
      continue
        
    if state[v] == 0:
      visit(v)
      
  state[u] = 2
  time += 1
  finished[u] = time

def dfs():
  global time
  time = 0
  
  for u in range(n):
    if state[u] == 0:
      visit(u)
          
n = int(input())

L = [[0]*n for i in range(n)]
state = [0]*n
visited = [0]*n
finished = [0]*n

for i in range(n):
  val = list(map(int, input().split()))
  
  for i in val[2:]:
    L[val[0] - 1][i - 1] = 1
    
dfs()

for u in range(n):
  print(f'{u+1} {visited[u]} {finished[u]}')
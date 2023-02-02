def bfs(id):
  q.append(id)
  d[id] = 0
  
  while q:
    u = q.pop()
    
    for v in range(n):
      if List[u][v] == 0:
        continue
      
      if d[v] != False:
        continue
      
      d[v] = d[u] + 1
      q.append(v)

n = int(input())
List = [[0]*n for i in range(n)]
q = []
d = [False]*n

for i in range(n):
  val = list(map(int, input().split()))
  
  for i in val[2:]:
    List[val[0] - 1][i - 1] = 1
    
bfs(0)

for i, j in enumerate(d):
  print(f'{i + 1} {j}')
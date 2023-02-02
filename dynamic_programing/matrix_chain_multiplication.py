n = int(input())

table = [[1000000]*n for i in range(n)]
matrix = []

for i in range(n):
  val = list(map(int, input().split()))
  if i == 0:
    matrix.append(int(val[0]))
  
  matrix.append(int(val[1]))

for i in range(n):
    table[i][i] = 0

for ii in range(1, n):
  for i in range(n):
    j = i + ii
    if j >= n:
      continue
    
    for k in range(i, j):
      table[i][j] = min(table[i][k] + table[k + 1][j] + matrix[i]*matrix[k + 1]*matrix[j + 1], table[i][j])
      
print(table[0][-1])
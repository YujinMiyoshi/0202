n = int(input())

for i in range(n):
  x = input()
  y = input()
  
  len_x = len(x)
  len_y = len(y)
  
  table = [[0]*(len_x + 1) for i in range(len_y + 1)]
  
  for i in range(len_y):
    for j in range(len_x):
      if y[i] == x[j]:
        table[i + 1][j + 1] = table[i][j] + 1
      else:
        table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
        
  print(table[-1][-1])
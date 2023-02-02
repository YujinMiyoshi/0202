import sys

def solve(y):
  if y == 8:
    for i in range(8):
      for j in range(8):
        print(c[i][j], end='')
      print()

    sys.exit()
    
  if a[y] == 1:
    solve(y + 1)
    
  for x in range(8):
    if b[x] == 0 and u[y + x] == 0 and v[y + (7 - x)] == 0:
      c[y][x] = 'Q'
      b[x] = u[y + x] = v[y + (7 - x)] = 1
      solve(y + 1)
      c[y][x] = '.'
      b[x] = u[y + x] = v[y + (7 - x)] = 0
      
n = int(input())

c = [['.']*8 for i in range(8)]
a = [0]*30
b = [0]*30
u = [0]*30
v = [0]*30

for i in range(n):
  y, x = map(int, input().split())
  c[y][x] = 'Q'
  u[y + x] = v[y + (7 - x)] = 1
  a[y] = b[x] = 1
  
solve(0)
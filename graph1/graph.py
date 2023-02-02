n = int(input())

gra = [[0]*n for i in range(n)]

for i in range(n):
  val = list(map(int, input().split()))
  
  if val[1] != 0:
    for j in val[2:]:
      gra[val[0] - 1][j - 1] = 1
      
for g in gra:
  print(*g)
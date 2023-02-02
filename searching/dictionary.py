arr = []
n = int(input())

for i in range(n):
  order = list(input().split())
  
  if order[0] == 'insert':
    arr.append(order[1])
    
  elif order[0] == 'find':
    if order[1] in arr:
      print('yes')
      
    else:
      print('no')
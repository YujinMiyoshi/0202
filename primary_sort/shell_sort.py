def insertion_sort(arr, n, g, cnt):
  for i in range(g, n):
    val = arr[i]
    j = i - g
    
    while j >= 0 and arr[j] > val:
      cnt += 1
      arr[j + g] = arr[j]
      j -= g
    
    arr[j + g] = val
    
  return cnt

def shell_sort(arr, n):
  cnt = 0
  m = 0
  g = n - 1
  
  G = []
  
  while g > 0:
    G.append(g)
    m += 1
    cnt = insertion_sort(arr, n, g, cnt)
    g //= 3
    
  print(m)
  print(*G)
  print(cnt)
  
  return G

arr = []

n = int(input())
for i in range(n):
  val = int(input())
  
  arr.append(val)
  
shell_sort(arr, n)

for i in arr:
  print(i)
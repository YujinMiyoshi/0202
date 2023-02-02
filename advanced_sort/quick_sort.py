def is_not_stable(arr, sorted, n):
  flag = False
  for i in range(n):
    for j in range(i+1, n):
      if arr[i][1] == arr[j][1]:
        for a in range(n):
          for b in range(a + 1, n):
            if not(arr[i] == sorted[a] and arr[j] == sorted[b]):
              flag = True
  return flag

def partition(arr, f, l):
  key = arr[l][1]
  i = f
  
  for j in range(f, l):
    if arr[j][1] <= key:
      arr[i], arr[j] == arr[j], arr[i]
      i += 1
      
  arr[i], arr[l] = arr[l], arr[i]
  
  return i

def quick_sort(arr, f, l):
  if f < l:
    m = partition(arr, f, l)
    quick_sort(arr, f, m - 1)
    quick_sort(arr, m + 1, l)
    
n = int(input())
arr = []

for i in range(n):
  val = list(input().split())
  val[1] = int(val[1])
  arr.append(val)
  
copy = arr[:]

quick_sort(arr, 0, n - 1)

flag = is_not_stable(copy, arr, n)

if flag:
  print('Not stable')
else:
  print('Stale')
  
for i in arr:
  print(*i)
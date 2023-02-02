inf = 10**6

def partition(arr, f, l):
  key = arr[l]
  i = f
  
  for j in range(f, l):
    if arr[j] <= key:
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
arr = list(map(int, input().split()))
arr_sorted = arr[:]

quick_sort(arr_sorted, 0, n - 1)

manage = [False]*n
next = {}

j = 0
for i in arr_sorted:
  next[i] = j
  j += 1

mini_w = min(arr)

cost = 0

for i in range(n):
  if manage[i] == 1:
    continue
  
  sum = n_g = 0
  
  while True:
    manage[i] = 1
    sum += arr[i]
    mini_g = min(inf, arr[i])
    n_g += 1
    i = next[arr[i]]
    
    if manage[i] == 1:
      break
        
  cost += min(mini_g*(n_g - 2) + sum, mini_g + sum + (1 + n_g)*mini_w)
  
print(cost)
    
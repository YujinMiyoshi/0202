import math

inf = 10**9

def merge_sort(arr, f, l, count):
  if f < l:
    m = math.floor((f + l)/2)
    
    count = merge_sort(arr, f, m, count)
    count = merge_sort(arr, m + 1, l, count)
    
    count = merge(arr, f, m, l, count)
    
  return count

def merge(arr, f, m, l, count):
  a = m - f + 1
  b = l - m
  
  left = [inf] * (a + 1)
  right = [inf] * (b + 1)
  
  for i in range(0, a):
    left[i] = arr[f + i]
    
  for j in range(0, b):
    right[j] = arr[m + j + 1]
    
  i = j = 0
  
  for k in range(f, l + 1):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
      
    elif left[i] > right[j]:
      arr[k] = right[j]
      j += 1
      
    count += 1

  return count

n = int(input())
arr = list(map(int, input().split()))
count = 0

count = merge_sort(arr, 0, n - 1, count)

print(*arr)
print(count)
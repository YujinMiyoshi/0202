def partition(arr, f, l):
  key = arr[l]
  i = f
  
  for j in range(f, l):
    if arr[j] <= key:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      
  arr[i], arr[l] = arr[l], arr[i]
  
  arr[i] = f'[{arr[i]}]'
  
n = int(input())
arr = list(map(int, input().split()))

partition(arr, 0, n - 1)

print(*arr)
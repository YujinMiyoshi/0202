def max_heap(arr, i):
  left = i*2
  right = i*2 + 1
  
  if left <= n and arr[left] > arr[i]:
    max = left
  else:
    max = i
    
  if right <= n and arr[right] > arr[max]:
    max = right
    
  if max != i:
    arr[i], arr[max] = arr[max], arr[i]
    
    max_heap(arr, max)
    
n = int(input())
arr = [False] + list(map(int, input().split()))

for i in range(n//2, 0, -1):
  max_heap(arr, i)
  
print('', *arr[1:])
def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  
def bubble_sort(arr, n):
  count = 0
  for i in range(n - 1):
    for j in range(n - 1, i, -1):
      if arr[j-1] > arr[j]:
        swap(arr, j-1, j)
        count += 1
        
  return count

n = int(input())
arr = list(map(int, input().split()))

count = bubble_sort(arr, n)

print(*arr)
  
print(count)
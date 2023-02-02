def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  
def selection_sort(arr, n, cnt):
  for i in range(n - 1):
    min = i
    for j in range(i, n):
      if arr[j] < arr[min]:
        min = j
    swap(arr, i, min)
    if i != min:
      cnt += 1
  
  return cnt

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
count = selection_sort(arr, n, cnt)

print(*arr)

print(count)
def insertion_s(arr, n):
  for i in range(1, n):
    val = arr[i]
    j = i - 1
    
    while arr[j] > val and j >= 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = val
    
    for i in range(n):
      print(arr[i], end=' ')
    print()
    
n = int(input())
arr = list(map(int, input().split()))

insertion_s(arr, n)
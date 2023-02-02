def exhaustive_search(n, m, arr):
  for i in m:
    if search(0, i, n, arr) == 1:
      print('yes')
    else:
      print('no')
      
def search(x, i, n, arr):
  if i == 0:
    return 1
  
  elif x >= n:
    return 0
  
  return search(x + 1, i, n, arr) or search(x + 1, i - arr[x], n, arr)

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

exhaustive_search(n, m, arr)
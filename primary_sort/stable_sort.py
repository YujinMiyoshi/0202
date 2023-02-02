def is_stable(arr, sorted, n):
  for i in range(n):
    for j in range(i+1, n):
      if sorted[i][1] == sorted[j][1]:
        for a in range(n):
            #print(arr[a])
            if arr[a][1] == sorted[i][1]:
              if arr[a] != sorted[i]:
                #print(arr[a][1], arr[a][0], sorted[i][1], sorted[i])
                return False
              else:
                break
  return True

def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  
def bubble_sort(arr, n):
  count = 0
  
  for i in range(n - 1):
    for j in range(n - 1, i, -1):
      if arr[j - 1][1] > arr[j][1]:
        swap(arr, j - 1, j)
        
        count += 1
        
  return count

def selection_sort(arr_1, n, cnt):
  for i in range(n):
    min = i
    
    for j in range(i, n):
      if arr_1[j][1] < arr_1[min][1]:
        min = j
        
    swap(arr_1, i, min)
    
    if i != min:
      cnt += 1
      
  return cnt

n = int(input())
arr = list(input().split())

copy = arr[:]

bubble_sort(arr, n)

judge = is_stable(copy, arr, n)

print(*arr)

if judge:
  print('Stable')
else:
  print('Not stable')
  
cnt = 0

copy_2 = copy[:]

selection_sort(copy, n, cnt)

judge = is_stable(copy_2, copy, n)

print(*copy)

if judge:
  print('Stable')
else:
  print('Not stable')
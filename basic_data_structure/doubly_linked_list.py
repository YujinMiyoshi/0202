from collections import deque

arr = deque([])

def insert_num(arr, num):
  arr.insert(0, num)
  
def delete_num(arr, num):
  arr.remove(num)
  
n = int(input())

for i in range(n):
  order = list(input().split())
  
  if order[0] == 'insert' or order[0] == 'delete':
    order[1] = int(order[1])
    
    if order[0] == 'insert':
      insert_num(arr, order[1])
      
    elif order[0] == 'delete':
      delete_num(arr, order[1])
      
  elif order[0] == 'deleteFirst':
    arr.popleft()
    
  elif order[0] == 'deleteLast':
    arr.pop()
    
print(*arr)
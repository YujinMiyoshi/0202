def extract(arr):
  max = arr[0] #配列の０番目をmaxにする
  for i in range(len(arr) - 1): #配列の長さ - 1回ループする
    if max < arr[i + 1]: #maxより配列のi + 1番目の方が大きければ
      max = arr[i + 1] #配列のi + 1番目をmaxにする
      
  print(max)
  
  arr.remove(max)

arr = []

while True:
  val = list(input().split())
  
  if val[0] == 'end':
    break
  
  elif val[0] == 'insert':
    key = int(val[1])
    arr.append(key)
    
  elif val[0] == 'extract':
    extract(arr)
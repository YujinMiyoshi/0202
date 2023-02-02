n = int(input())
arr_1 = [0]*n
arr_2 = []

for i in range(n):
  arr_1[i] = int(input())
  
for i in range(n - 1):
  for j in range(i + 1, n):
    val = arr_1[j] - arr_1[i]
    
    arr_2.append(val)
    
arr_2.sort()

maximum_profit = arr_2[len(arr_2) - 1]

print(maximum_profit)
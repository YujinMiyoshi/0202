n = int(input())
arr_1 = list(map(int, input().split()))
max = max(arr_1)
arr_2 = [0]*(max + 1)
arr_3 = [None]*(n + 1)

for i in arr_1:
  arr_2[i] += 1
  
for i in range(1, max + 1):
  arr_2[i] += arr_2[i - 1]
  
for i in arr_1:
  arr_3[arr_2[i]] = i
  arr_2[i] -= 1
  
print(*arr_3[1:])
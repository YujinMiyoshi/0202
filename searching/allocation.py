sum = 0
n, k = map(int, input().split())

for i in range(n):
  val = int(input())
  sum += val
  
q = sum // k
r = sum % k

max = q + r

print(max)
def is_prime(num):
  if num == 2:
    return True
  
  for i in range(2, num):
    if (num % i) == 0:
      return False
  return True
  
n = int(input())
count = 0

for i in range(n):
  num = int(input())
  flag = is_prime(num)
  
  if flag:
    count += 1
    
print(count)
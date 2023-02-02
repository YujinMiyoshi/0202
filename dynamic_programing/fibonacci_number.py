fib = []
n = int(input())

n += 1

if n < 3:
  print(1)

else:
  for i in range(2):
    fib.append(1)
  
  for i in range(2, n): #roop n times
    fib.append(fib[i - 1] + fib[i - 2]) #put the sum of previous array key and the previous array key of it in the array fib
    
  print(fib[n - 1])
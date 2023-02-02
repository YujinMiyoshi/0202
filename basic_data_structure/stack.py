def rev_pol(formula):
  stack = []
  ope = ['+', '-', '*', '/']
  
  for i in formula.split(' '):
    if i in ope:
      y, x = stack.pop(), stack.pop()
      result = eval(f'{x} {i} {y}')
      stack.append(result)
      
    else:
      stack.append(int(i))
      
  return stack.pop()

formula = input()

result = rev_pol(formula)

print(result)
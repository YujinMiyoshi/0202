region = list(input())

descent, flood = [], []

count = 0

for i in region:
  count += 1
  
  if i == '\\':
    descent.append(count)
    
  elif i == '/' and descent:
    no_flood = descent.pop()
    flood_area = count - no_flood
    
    while flood and flood[-1][0] > no_flood:
      flood_area += flood.pop()[1]
      
    flood.append([no_flood, flood_area])
    
A = 0
for i in flood:
  A += i[1]
  
k = len(flood)

print(A)
print(k, *(i[1] for i in flood))
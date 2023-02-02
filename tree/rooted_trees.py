class node:
  def __init__(self, parent, left, right):
    self.parent = parent
    self.left = left
    self.right = right
    
def get_depth(nodes, id, p):
  dep[id] = p
  
  if nodes[id].right is not False:
    get_depth(nodes, nodes[id].right, p)
      
  if nodes[id].left is not False:
    get_depth(nodes, nodes[id].left, p + 1)
      
def get_children(nodes, id):
  children = []
  child = nodes[id].left
    
  while child is not False:
    children.append(child)
    child = nodes[child].right
      
  return children
  
dep = {}
n = int(input())
nodes = {i: node(False, False, False) for i in range(n)}

for i in range(n):
  val = list(map(int, input().split()))
  
  if val[1] == 0:
    continue
  
  nodes[val[0]].left = val[2]
  nodes[val[2]].parent = val[0]

  pre = val[2]
  
  for i in val[3:]:
    nodes[pre].right = i
    nodes[i].parent = val[0]
    pre = i
  
  for id in range(n):
    if nodes[id].parent is False:
      get_depth(nodes, id, 0)
      
      break
    
for id in range(n):
  print(f'node {id}: ', end='')
  
  if nodes[id].parent is False:
    print(f'parent = {-1}, ', end='')
  else:
    print(f'parent = {nodes[id].parent}, ', end='')
    
  print(f'depth = {dep[id]}, ', end='')
  
  if nodes[id].parent is False:
    print('root, ', end='')
  elif nodes[id].left is not False:
    print('internal node, ', end='')
  else:
    print('leaf, ', end='')
    
  children = get_children(nodes, id)
  print(children)
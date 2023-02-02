dep = {}
hi = {}

class node:
  def __init__(self, parent, left, right):
    self.parent = parent
    self.left = left
    self.right = right
    
def get_depth(nodes, id, p):
  dep[id] = p
  
  if nodes[id].left is not False:
    get_depth(nodes, nodes[id].left, p + 1)
    
  if nodes[id].right is not False:
    get_depth(nodes, nodes[id].right, p + 1)
    
def get_hight(nodes, id):
  l = r = 0
  
  if nodes[id].left is not False:
    l = get_hight(nodes, nodes[id].left) + 1
    
  if nodes[id].right is not False:
    r = get_hight(nodes, nodes[id].right) + 1
    
  h = max(l, r)
  hi[id] = h
  
  return h

def get_bro(nodes, id):
  parent = nodes[id].parent
  
  if parent is not False:
    if nodes[parent].left != id:
      bro = nodes[parent].left
    else:
      bro = nodes[parent].right
      
  else:
    return -1
  
  if bro:
    return bro
  
  return 0

def get_number(nodes, id):
  num = 0
  
  if nodes[id].left:
    num += 1
  
  if nodes[id].right:
    num += 1
    
  return num

n = int(input())
nodes = {i: node(False, False, False) for i in range(n)}

for i in range(n):
  val = list(map(int, input().split()))
  
  if val[1] != -1:
    nodes[val[0]].left = val[1]
    nodes[val[1]].parent = val[0]
    
  if val[2] != -1:
    nodes[val[0]].right = val[2]
    nodes[val[2]].parent = val[0]
    
for id in range(n):
  if nodes[id].parent is False:
    get_depth(nodes, id, 0)
    get_hight(nodes, id)
    
    break
  
for id in range(n):
  print(f'node {id}: ', end='')
  
  type = False
  
  if nodes[id].parent is False:
    print(f'parent = {-1}, ', end='')
    type = 'root'
    
  else:
    print(f'parent = {nodes[id].parent}, ', end='')
    
  bro = get_bro(nodes, id)
  num = get_number(nodes, id)
  
  print(f'sibling = {bro}, degree = {num}, depth = {dep[id]}, height = {hi[id]}, ', end='')
  
  if type is False:
    if num != 0:
      print('internal node')
      
    else:
      print('leaf')
      
  else:
    print(type)
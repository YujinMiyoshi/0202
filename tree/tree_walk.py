pre_arr = []
in_arr = []
post_arr = []

class node:
  def __init__(self, parent, left, right):
    self.parent = parent
    self.left = left
    self.right = right
    
def pre_order(nodes, id, pre_arr):
  if id is False:
    return
  
  pre_arr.append(id)
  pre_order(nodes, nodes[id].left, pre_arr)
  pre_order(nodes, nodes[id].right, pre_arr)
  
def in_order(nodes, id, in_arr):
  if id is False:
    return
  
  in_order(nodes, nodes[id].left, in_arr)
  in_arr.append(id)
  in_order(nodes, nodes[id].right, in_arr)
  
def post_order(nodes, id, post_arr):
  if id is False:
    return
  
  post_order(nodes, nodes[id].left, post_arr)
  post_order(nodes, nodes[id].right, post_arr)
  post_arr.append(id)
  
n = int(input())
nodes = {i: node(False, False, False) for i in range(n)}

for i in range(n):
  val = list(map(int, input().split()))
  
  for j in range(len(val)):
    if val[j] == -1:
      val[j] = False
  
  nodes[val[0]].left = val[1]
  nodes[val[0]].right = val[2]
  
  if nodes[val[0]].parent is False:
    root = val[0]
    
  if val[1] is not False:
    nodes[val[1]].parent = val[0]
    
  if val[2] is not False:
    nodes[val[2]].parent = val[0]
    
pre_order(nodes, root, pre_arr)
in_order(nodes, root, in_arr)
post_order(nodes, root, post_arr)

print('Preorder')
print('', *pre_arr)

print('Inorder')
print('', *in_arr)

print('Postorder')
print('', *post_arr)
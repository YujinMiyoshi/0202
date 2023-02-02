class node:
    def __init__(self, parent=False, left=False, right=False):
        self.parent = parent
        self.left = left
        self.right = right

def pre_search(nodes, id, pre_arr):
    if id is False:
        return

    pre_arr.append(id)
    pre_search(nodes, nodes[id].left, pre_arr)
    pre_search(nodes, nodes[id].right, pre_arr)

def in_search(nodes, id, in_arr):
    if id is False:
        return

    in_search(nodes, nodes[id].left, in_arr)
    in_arr.append(id)
    in_search(nodes, nodes[id].right, in_arr)

def insert(nodes, root, id):
    if root == id:
        nodes[id] = node()

    else:
        nodes[id] = node()
        key = root

        while key is not False:
            next_parent = key

            if id < key:
                key = nodes[key].left
            else:
                key = nodes[key].right

        nodes[id].parent = next_parent

        if id < next_parent:
            nodes[next_parent].left = id
        else:
            nodes[next_parent].right = id

def print_ans(nodes):
    pre_arr, in_arr = [], []

    pre_search(nodes, root, pre_arr)
    in_search(nodes, root, in_arr)

    for i in in_arr:
        print(' ' + str(i), end='')
    print()

    for i in pre_arr:
        print(' ' + str(i), end='')
    print()
"""
    print(' ', *in_arr)
    print(' ', *pre_arr)
"""
n = int(input())
nodes = {}

for i in range(n):
    val = list(input().split())

    if val[0] == 'insert':
        id = int(val[1])

        if i == 0:
            root = id

        insert(nodes, root, id)

    elif val[0] == 'print':
        print_ans(nodes)
class node:
    def __init__(self, pearent=False, left=False, right=False):
        self.parent = pearent
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
    nodes[id] = node()

    if root == id:
        return

    else:
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

def find(nodes, root, id):
    key = root

    while key is not False and id != key:
        if id < key:
            key = nodes[key].left
        else:
            key = nodes[key].right

    return key

def print_ans(nodes):
    pre_arr = []
    in_arr = []

    pre_search(nodes, root, pre_arr)
    in_search(nodes, root, in_arr)

    print('', *in_arr, '\n' '', *pre_arr)

n = int(input())
nodes = {}

for i in range(n):
    val = list(input().split())

    if val[0] == 'insert':
        id = int(val[1])

        if i == 0:
            root = id

        insert(nodes, root, id)

    elif val[0] == 'find':
        id = int(val[1])

        flg = find(nodes, root, id)

        if flg:
            print('yes')
        else:
            print('no')

    else:
        print_ans(nodes)
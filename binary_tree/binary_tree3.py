class node:
    def __init__(self, parent=False, left=False, right=False):
        self.parent = parent
        self.left = left
        self.right = right

def pre_search(nodes, id, pre_arr):
    if id == False:
        return

    pre_arr.append(id)
    pre_search(nodes, nodes[id].left, pre_arr)
    pre_search(nodes, nodes[id].right, pre_arr)

def in_search(nodes, id, in_arr):
    if id == False:
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
            next = key

            if id < key:
                key = nodes[key].left
            else:
                key = nodes[key].right

        nodes[id].parent = next

        if id < next:
            nodes[next].left = id
        else:
            nodes[next].right = id

def find(nodes, root, id):
    key = root

    while key is not False and key != id:
        if id < key:
            key = nodes[key].left
        else:
            key = nodes[key].right

    return key

def delete(nodes, id):
    parent = nodes[id].parent

    if (nodes[id].left is False) and (nodes[id].right is False):
        if nodes[parent].left == id:
            nodes[parent].left = False
        else:
            nodes[parent].right = False

        del nodes[id]

        return

    elif nodes[id].left is False:
        if nodes[id].left == id:
            leftId = True
        else:
            leftId = False

        if leftId:
            nodes[parent].left = nodes[id].right
        else:
            nodes[parent].right = nodes[id].right

        nodes[nodes[id].right].parent = parent

        del nodes[id]

        return

    elif nodes[id].right is False:
        if nodes[id].left == id:
            leftId = True
        else:
            leftId = False

        if leftId:
            nodes[parent].left = nodes[id].left
        else:
            nodes[id].right = nodes[id].left

        nodes[nodes[id].left].parent = parent

        del nodes[id]

        return

    elif (nodes[id].left is not False) and (nodes[id].right is not False):
        left = nodes[id].left
        right = nodes[id].right

        node_des = get_min(nodes, nodes[id].right)

        if parent is False:
            if node_des == right:
                nodes[right].parent = False
                nodes[right].left = left
                root = right

                del nodes[id]

                return

            else:
                nodes[node_des].left = left
                nodes[left].parent = node_des
                nodes[node_des].right = right
                nodes[right].parent = node_des
                nodes[node_des].parent = False

                if nodes[node_des].right is not False:
                    nodes[nodes[node_des].right].parent = node_des

                root = node_des

                del nodes[id]

                return

        else:
            if nodes[parent].left == id:
                leftId = True
            else:
                leftId = False

            if node_des == right:
                nodes[right].parent = parent
                nodes[right].left = left

                if leftId:
                    nodes[parent].left = right
                else:
                    nodes[parent].right = right

                del nodes[id]

                return

            else:

                nodes[node_des].left = nodes[id].left
                nodes[left].parent = node_des
                nodes[node_des].right = nodes[id].right
                nodes[right].parent = node_des
                nodes[node_des].parent = nodes[id].parent

                if leftId:
                    nodes[parent].left = node_des
                else:
                    nodes[parent].right = node_des

                nodes[nodes[node_des].parent].left = nodes[node_des].right

                if nodes[node_des].right is not False:
                    nodes[nodes[node_des].right].parent = nodes[node_des].parent

                del nodes[id]

                return

def get_min(nodes, id):
    key = id

    while nodes[key].left is not False:
        key = nodes[key].left

    return key

def print_ans(nodes):
    pre_arr = []
    in_arr = []

    pre_search(nodes, root, pre_arr)
    in_search(nodes, root, in_arr)

    print('', *in_arr)
    print('', *pre_arr)

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

        if find(nodes, root, id) is not False:
            print('yes')
        else:
            print('no')

    elif val[0] == 'delete':
        id = int(val[1])
        delete(nodes, id)

    else:
        print_ans(nodes)
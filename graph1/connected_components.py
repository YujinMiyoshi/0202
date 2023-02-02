from collections import defaultdict

def dfs(u, id):
    q.append(u)
    state[u] = id

    while q:
        u = q.pop()

        for v in p[u]:
            if state[v] == -1:
                state[v] = id
                q.append(v)

n, m = map(int, input().split())

state = [-1]*n
q = []
p = defaultdict(lambda: [])

for i in range(m):
    s, t = map(int, input().split())
    p[s].append(t)
    p[t].append(s)

for id, u in enumerate(state, 1):
    if u == -1:
        dfs(id - 1, id)

question = int(input())

for i in range(question):
    s, t = map(int, input().split())

    if state[s] == state[t]:
        print('yes')
    else:
        print('no')
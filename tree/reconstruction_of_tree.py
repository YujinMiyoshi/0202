post_arr = []
key = 0

def reconstruction(f, l):
    global key

    if f >= l:
        return

    mid = pre_arr[key]

    j = 0
    for i in in_arr:
        if i == mid:
            m = j
            break

        j += 1

    key += 1

    reconstruction(f, m)
    reconstruction(m + 1, l)

    post_arr.append(mid)

n = int(input())
pre_arr = list(map(int, input().split()))
in_arr = list(map(int, input().split()))

reconstruction(0, n)

print(*post_arr)
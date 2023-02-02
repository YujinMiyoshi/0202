import math

inf = 10**9

def merge_sort(arr, f, l):
    if f + 1 >= l:
        return 0

    m = math.floor((f + l)/2)

    sum1 = merge_sort(arr, f, m)
    sum2 = merge_sort(arr, m, l)

    sum3 = merge(arr, f, m, l)

    sum = sum1 + sum2 + sum3

    return sum

def merge(arr, f, m, l):
    count = 0
    n = m - f

    arr_f = arr[f:m]
    arr_f.append(inf)

    arr_l = arr[m:l]
    arr_l.append(inf)

    i = j = 0

    for k in range(f, l):
        if arr_f[i] <= arr_l[j]:
            arr[k] = arr_f[i]
            i += 1

        else:
            arr[k] = arr_l[j]
            j += 1

            count += n - i

    return count

n = int(input())
arr = list(map(int, input().split()))

count = merge_sort(arr, 0, n)

print(count)
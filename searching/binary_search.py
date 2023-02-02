import math

def binary_search(arr, key, f, l):
    if f > l:
        return 0

    else:
        m = math.floor((f + l)/2)

        if arr[m] > key:
            return binary_search(arr, key, f, m - 1)

        elif arr[m] < key:
            return binary_search(arr, key, m + 1, l)

        else:
            return 1

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
arr2 =list(map(int, input().split()))

count = 0

for i in arr2:
    count += binary_search(arr, i, 0, n - 1)

print(count)
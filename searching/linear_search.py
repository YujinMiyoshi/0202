def linear_search(arr, key):
    for i in arr:
        if i == key:
            return 1

    return 0

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
arr2 = list(map(int, input().split()))

count = 0

for i in arr2:
    count += linear_search(arr, i)

print(count)
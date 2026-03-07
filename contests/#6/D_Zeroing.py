n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
val, idx = 0, 0

for _ in range(k):
    if idx == len(arr):
        print(0)
        continue

    print(arr[idx] - val)
    val += arr[idx] - val

    idx += 1
    while idx < len(arr) and arr[idx] - val == 0:
        idx += 1
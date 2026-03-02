t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left, mid, right = arr[0], arr[1], arr[2]
    operations = (mid - left) + (right - mid)
    print(operations)
            
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    minOp = arr[-1]

    for i in range(2, n):
        minOp = min(minOp, arr[i] - arr[i - 2])
    print(minOp)
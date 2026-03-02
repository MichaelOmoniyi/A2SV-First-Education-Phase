t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    pos = True
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            pos = False
            break
    if pos:
        print("YES")
    else:
        print("NO")
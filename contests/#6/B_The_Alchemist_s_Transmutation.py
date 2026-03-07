t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    y = int(input())

    if max(arr) >= y and min(arr) <= y:
        print("YES")
    else:
        print("NO")
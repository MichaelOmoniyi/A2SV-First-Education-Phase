t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    m = k // 2

    if 2 * m == n:
        for i in range(1, n, 2):
            if a[i] != (i + 1) // 2:
                print((i + 1) // 2)
                break
        print(m + 1)
    else:
        limit = n - 2 * m + 1
        for i in range(1, limit):
            if a[i] != 1:
                print(1)
                break
        print(2)
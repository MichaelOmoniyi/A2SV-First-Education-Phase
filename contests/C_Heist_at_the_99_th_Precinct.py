t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = 0
    diag = False
    print("Testcase: ", _)
    for i in range(n):
        if arr[i] >= mx:
            mx = arr[i]
            arr[i] = 0

            if i % 2 == 0:
                diag = True
                print("Diag leading")
            else:
                diag = False
                print("Diag losing")
        print(arr)
        print(mx)
    if diag is False:
        print("NO")
    else:
        print("YES")
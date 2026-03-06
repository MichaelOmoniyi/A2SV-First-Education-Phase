n = int(input())
arr = list(map(int, input().split()))

even, odd = 0, 0

for i in range(n):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if even == 0 or odd == 0:
    print(" ".join(map(str, arr)))
else:
    arr.sort()
    print(" ".join(map(str, arr)))
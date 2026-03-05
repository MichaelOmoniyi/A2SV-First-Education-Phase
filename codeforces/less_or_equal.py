n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# Exactly zero elements must be less than x
# x must be less than all the element but within the range provided
if k == 0:
    if arr[0] < 2:
        print(-1)
    else:
        print(arr[0] - 1)
elif k == n: # Exactly k elements must be less than or equal to x which is the max number
    print(arr[-1] + 1)
else:
    if arr[k - 1] == arr[k]:
        print(-1)
    else:
        print(arr[k - 1] + 1)
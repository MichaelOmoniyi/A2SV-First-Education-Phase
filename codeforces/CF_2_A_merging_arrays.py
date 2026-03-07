n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = arr1 + [0] * m

i, j = len(arr1) - 1, m - 1

while j >= 0:
    if arr1[n-1] > arr2[j] and n > 0:
        arr1[i] = arr1[n-1]
        i -= 1
        n -= 1
    else:
        arr1[i] = arr2[j]
        i -= 1
        j -= 1
print(" ".join(map(str, arr1)))
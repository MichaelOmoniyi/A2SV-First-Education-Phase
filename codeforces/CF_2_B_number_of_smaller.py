n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

first, count = 0, 0
smaller = []

for second in range(len(arr2)):
    while first <= len(arr1) - 1 and arr1[first] < arr2[second]:
        count += 1
        first += 1
    smaller.append(count)
print(" ".join(map(str, smaller)))
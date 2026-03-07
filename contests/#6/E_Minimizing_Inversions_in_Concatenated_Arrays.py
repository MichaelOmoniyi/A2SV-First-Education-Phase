t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (min(x), max(x)))
    print(" ".join(map(str, [x for pair in arr for x in pair])))
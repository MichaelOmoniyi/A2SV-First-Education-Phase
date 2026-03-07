from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    freq = Counter(list(map(int, input().split())))

    for i in freq:
        if freq[i] % 2 == 1:
            print("YES")
            break
    else:
        print("NO")
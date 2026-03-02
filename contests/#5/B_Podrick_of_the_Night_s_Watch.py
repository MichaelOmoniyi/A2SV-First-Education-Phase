n = int(input())
pairCount = {}

for _ in range(n):
    for _ in range(int(input())):
        ravenName, hour = list(input().split())
        pairCount[(ravenName, hour)] = pairCount.get((ravenName, hour), 0) + 1

for pair in pairCount:
    RCR = (pairCount[pair] / n) * 100
    if RCR >= 80:
        print("YES")
        break
else:
    print("NO")
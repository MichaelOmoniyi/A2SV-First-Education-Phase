n, t = map(int, input().split())
readTime = list(map(int, input().split()))
maxSum = 0
window = 0
left = 0

for i in range(n):
    maxSum += readTime[i]
    if maxSum > t:
        maxSum -= readTime[left]
        left += 1
    else:
        window += 1
print(window)
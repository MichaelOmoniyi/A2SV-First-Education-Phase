t = int(input())

for _ in range(t):
    print("Test case", _ + 1)
    arrLen, operations = map(int, input().split())
    arr = list(map(int, input().split()))
    maxElement = []
    
    for i in range(operations):
        print("Operation", i + 1)
        symbol, l, r = input().split()
        l, r = int(l), int(r)

        for j in range(max(0, l), min(arrLen, r + 1)):
            if symbol == "+":
                arr[j] += 1
            else:
                arr[j] -= 1
        maxElement.append(max(arr))
        print(arr)
        print("Max element:", maxElement[-1])
        print("Max array after operation", i + 1, ":", maxElement)
    
    for element in maxElement:
        print(element, end=" ")
    print()
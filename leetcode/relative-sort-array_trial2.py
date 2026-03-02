class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countDict = {}
        notInArr2 = []

        # Initialize counts
        for ele in arr2:
            countDict[ele] = 0
        
        for num in arr1:
            if num in countDict:
                countDict[num] += 1
            else:
                notInArr2.append(num)

        # Rearrange arr1 according to arr2 order
        target = 0
        for j in range(len(countDict)):
            for _ in range(countDict[arr2[j]]):
                arr1[target] = arr2[j]
                target += 1
            print(arr1)

        # Sort remaining elements
        notInArr2.sort()

        return arr1[:target] + notInArr2
        
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                j = len(arr) - 1
                while j > i and j > 0:
                    if j == (i + 1):
                        arr[j] = 0
                    else:
                        arr[j] = arr[j - 1]
                    j -= 1
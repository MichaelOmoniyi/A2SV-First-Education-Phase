class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        def sign(a, b):
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        
        maxLen = 1
        currLen = 1
        prevSign = 0
        
        for i in range(1, n):
            currSign = sign(arr[i-1], arr[i])
            
            if currSign == 0:
                currLen = 1
            elif currSign * prevSign == -1:
                currLen += 1
            else:
                currLen = 2  # restart from previous pair
            
            maxLen = max(maxLen, currLen)
            prevSign = currSign
        
        return maxLen
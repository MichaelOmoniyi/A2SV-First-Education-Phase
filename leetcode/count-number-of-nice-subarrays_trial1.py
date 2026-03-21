from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        
        oddCount = 0
        res = 0
        
        for num in nums:
            if num % 2 == 1:
                oddCount += 1
            
            if (oddCount - k) in prefixCount:
                res += prefixCount[oddCount - k]
            
            prefixCount[oddCount] += 1
        
        return res
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        left, windowSum, res = 0, 0, 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            windowSum += nums[right]
            
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                windowSum -= nums[left]
                left += 1
            
            if right - left + 1 == k and len(freq) == k:
                res = max(res, windowSum)
        
        return res
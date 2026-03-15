class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        maxSum = -float("inf")
        left = 0

        for i in range(k):
            window += nums[i]
        maxSum = max(maxSum, window)

        for j in range(i+1, len(nums)):
            window += nums[j]
            window -= nums[left]
            left += 1
            maxSum = max(maxSum, window)
        return maxSum / k